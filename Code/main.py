import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt
import readDat
import filePath
import os
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

    stacked_data = df2015.append(df2016)
    stacked_data = stacked_data.append(df2017)

    region_df = df2016[['Country', 'Region']]
    df2017 = df2017.merge(region_df, how='left', on='Country')
    




if __name__=="__main__":
    main()


