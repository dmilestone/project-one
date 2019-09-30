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

crime_2014_df = crime_df.loc[crime_df["Year"] == "2014"]
# crime_2015_df = crime_df.loc[crime_df["Year"] == "2015"]
# crime_2016_df = crime_df.loc[crime_df["Year"] == "2016"]
# crime_2017_df = crime_df.loc[crime_df["Year"] == "2017"]
# crime_2018_df = crime_df.loc[crime_df["Year"] == "2018"]

x = crime_2014_df["Longitude"]
y = crime_2014_df["Latitude"]

plt.scatter(x, y, alpha=.005)

npu_outlines = []
for npu in data:
	npu_outlines.append(npu["geometry"]["coordinates"][0])

for value in npu_outlines:
	x = [outline[0] for outline in value]
	y = [outline[1] for outline in value]
	plt.plot(x, y)
plt.show()