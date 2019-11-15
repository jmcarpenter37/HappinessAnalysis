import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt
import readDat
import filePath
import os
import folium as fol
from folium import *
from folium.plugins import heat_map
import Mapper
def main():
    try:
        os.chdir(filePath.path["path"])
    except NotADirectoryError as err:
        print("That's not a valid path on this machine.")
        print("Error: {}".format(err))
    # CSV file path here
    # User will need to change the path of where the CSV files live.
    # read each csv into a pandas dataframes
    df2015 = readDat.csv_to_dataframe(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2015.csv")
    df2016 = readDat.csv_to_dataframe(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2016.csv")
    df2017 = readDat.csv_to_dataframe(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2017.csv")
    # Data cleansing
    # Rename years
    df2015['year']=2015
    df2016['year']=2016
    df2017['year']=2017
    #
    df2017 = df2017.rename(columns={'Happiness.Rank': 'Happiness Rank', 'Happiness.Score': 'Happiness Score',
                                    'Economy..GDP.per.Capita.':'Economy (GDP per Capita)',  'Health..Life.Expectancy.':'Health (Life Expectancy)',
                                    'Trust..Government.Corruption.':'Trust (Government Corruption)','Dystopia.Residual':'Dystopia Residual'})
    df2017 = df2017.replace(to_replace="Hong Kong S.A.R., China" , value ="Hong Kong")
    df2017 = df2017.replace(to_replace="Taiwan Province of China",value ="Taiwan")
    # Stacking the data into one pandas df
    stacked_data = df2015.append(df2016)
    stacked_data = stacked_data.append(df2017)
    region_df = df2016[['Country', 'Region']]
    stacked_data = df2017.merge(region_df, how='left', on='Country')
    # printing country
    print(stacked_data['Country'])
    # Lets get a map
    #map=fol.Map(location=[40.693 , -73.985] , control_scale=True, zoom_control=12)
    #fol.Marker(location=[40.693 , -73.985] , popup="Put some data in here. Data data data dat data dat dat dat dat dat dat dat dat" ,icon=fol.Icon() ).add_to(map)
    #map.save("my_map.html")
    #for country in range(len(stacked_data["Country"])):
    #    print(stacked_data["Country"][country])
    #    Mapper.pos_print( stacked_data["Country"][country])
    # We need to initialize a map object and then loop throught the ith+1 : len(data) value
    # I'll explain why I did it this way
    global MyMap # Create a global variable that the for loop below has access to
    MyMap = fol.Map() # Create an empy map object
    for country in range(len(stacked_data["Country"])):
        position = Mapper.pos_print(stacked_data["Country"][country])
        #print(position[0] , position[1])
        print(country)
        #map = fol.Map(location=[position[0],position[1]] , control_scale=True,zoom_control=12)
        fol.Marker(location=[position[0],position[1]] , popup="{}".format(country),icon=fol.Icon()).add_to(MyMap) # Add pinpoints to the mal
    MyMap.save("Pinpoints_Map.html") # Save the map as an html file

if __name__=="__main__":
    main()


