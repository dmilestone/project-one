import pandas as pd
import matplotlib.pyplot as plt
import os
import dateutil.parser as parser
import requests
from pprint import pprint
import matplotlib.lines as lines

response = requests.get('https://gis.atlantaga.gov/dpcd/rest/services/OpenDataService/FeatureServer/3/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryPolyline&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&gdbVersion=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=&f=geojson')
data = response.json()
data = data["features"]

crime_file = os.path.join("Resources", "COBRA-2009-2018.csv")
crime_df = pd.read_csv(crime_file)

crime_df["Year"] = [str(parser.parse(date).year) for date in crime_df["Occur Date"]]

npu_outlines = []
for npu in data:
	npu_outlines.append(npu["geometry"]["coordinates"][0])
npu_outlines.pop()

def write_crime_jpeg(year):
	xmin = 500
	ymin = 500
	xmax = -500
	ymax = -500

	for value in npu_outlines:
		if (len(value) == 1):
			break
		xs = [outline[0] for outline in value]
		current_xmin = min(xs)
		current_xmax = max(xs)
		if (current_xmin < xmin):
			xmin = current_xmin
		if (current_xmin > xmax):
			xmax = current_xmax

		ys = [outline[1] for outline in value]
		current_ymin = min(ys)
		current_ymax = max(ys)
		if (current_ymin < ymin):
			ymin = current_ymin
		if (current_ymax > ymax):
			ymax = current_ymax
		plt.plot(xs, ys)

	crime_year_df = crime_df.loc[crime_df["Year"] == year]
	crime_year_df = crime_year_df[crime_year_df["Longitude"] < xmax]
	crime_year_df = crime_year_df[crime_year_df["Longitude"] > xmin]
	crime_year_df = crime_year_df[crime_year_df["Latitude"] < ymax]
	crime_year_df = crime_year_df[crime_year_df["Latitude"] > ymin]

	x = crime_year_df["Longitude"]
	y = crime_year_df["Latitude"]

	plt.scatter(x, y, alpha=.005)
	plt.savefig(f"./year-over-year-scatter-plots/crime_{year}")
	plt.close()

write_crime_jpeg("2014")
write_crime_jpeg("2015")
write_crime_jpeg("2016")
write_crime_jpeg("2017")
write_crime_jpeg("2018")


