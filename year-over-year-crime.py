import pandas as pd
import matplotlib.pyplot as plt
import os
import dateutil.parser as parser
import requests
from pprint import pprint
import matplotlib.lines as lines

response = requests.get('https://arcgis.atlantaregional.com/arcgis/rest/services/OpenData/FeatureServer/196/query?where=1%3D1&outFields=*&outSR=4326&f=json')
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

x = crime_2014_df["Latitude"]
y = crime_2014_df["Longitude"]

plt.scatter(y, x, alpha=.01)
for npu in data:
	rings = npu["geometry"]["rings"]
	x = [ring[0] for ring in rings[0]]
	y = [ring[1] for ring in rings[0]]
	plt.plot(x, y)
plt.show()