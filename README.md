# Atlanta Crime and Home Values by Neighborhood (NPU) Analysis

## Questions
1. Which Atlanta neighborhoods have the highest median home values? 
2. Which Atlanta neighborhoods have the lowest median home values? 
3. Is there less crime in neighborhoods with highest median home values?
4. Is there more crime in neighborhoods with lowest median home values?
5. Is crime increasing or decreasing in neighborhoods with the highest and lowest median home values?

## Datasets
* Crime Data from Atlanta Police Department: 
https://www.atlantapd.org/i-want-to/crime-data-downloads
* Population Census data from atlantaga.gov: 
https://www.atlantaga.gov/government/departments/city-planning/office-of-zoning-development/population
* Home Value data collected by webscraping Niche.com: 
https://github.com/dmilestone/project-one/blob/master/Resources/niche.csv

## Tasks
### Webscraping Median Home Value by neighborhood - atl_home_values_by_neighborhood.ipynb
1. Pull each unique neighborhood from Atlanta crime data.
2. Webscrape Niche.com for median home value price (or Niche Price) for each Atlanta neighborhood.

### Full Analysis - percapitacode.ipynb
1. Read population data, niche data, and crime data using pandas.
2. Use datetime library to create new column with year from each crime occurrence record.
3. Use loc method to issolate crime incidents for each year from 2014-2018.
4. Ues count to calculate number of crime incidents for each year by neighborhood. 
5. Merge crime count by year, niche home value data, and population by neighborhood data into once dataframe.
6. Calculate crime incident per capita (per 100,000 people) for each neighborhood by dividing crime count by population and then multiplying by 100,000.
7. Drop null values that were created since some neighborhoods (NPUs) were combined in census data.
8. Create new column for change in crime per capita by subtracting 2014 counts from 2018 counts.
9. Create function to change Niche Price to float for calculation.
10. Create scatter plot using matplotlib to show crime incident count vs. median home values.
11. Use matplotlib to create line graph of crime trend from 2014 to 2018 for neighborhoods with top 5 median home values.
12. Use matplotlib to create line graph of crime trend from 2014 to 2018 for neighborhoods with lowest 5 median home values.

## Observations, Trends, Conclusions
1. The 5 Atlanta neighborhoods with highest median home value were: Kingswood, Argonne Forest, Margaret Mitchell, Mt. Paran/Northside, and West Paces Ferry/Northside
2. The 5 Atlanta neighborhoods with lowest median home values were: Carey Park, Almond Park, Pittsburgh, Hunter Hills, and Ashview Heights.
3. The top 5 neighborhoods saw signifigant less crime incidents per capita (all under 4,000 for each of the 5 years) than the average for all neighborhoods which ranged from 6,000-7,000 incidents per capita over the 5 year period.
4. Crime incidents had no correlation to median home value in the lowest 5 neighborhoods as crime rates were found to be above and below the average for all neighborhoods.
5. Neighborhoods with the 5 lowest median home values all had downward trends in crime over the five year period, while no consistent upward or downward trends were found among the top five neighborhoods. 


## Disclaimer

This project was published for educational purposes only. Copyright Trilogy Education Services © 2019. All Rights Reserved.
