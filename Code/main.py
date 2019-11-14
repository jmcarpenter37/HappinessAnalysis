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
    # Need to look into each CSV and find the discrepancies
    # Get the keys
    #print(df2015.keys()) # ['Country', 'Region', 'Happiness Rank', 'Happiness Score','Standard Error', 'Economy (GDP per Capita)', 'Family','Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity', 'Dystopia Residual']
    #print(df2016.keys()) # ['Country', 'Region', 'Happiness Rank', 'Happiness Score','Lower Confidence Interval', 'Upper Confidence Interval', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']
    #print(df2017.keys()) # ['Country', 'Happiness.Rank', 'Happiness.Score', 'Whisker.high', 'Whisker.low', 'Economy..GDP.per.Capita.', 'Family', 'Health..Life.Expectancy.', 'Freedom', 'Generosity', 'Trust..Government.Corruption.', 'Dystopia.Residual']
    # We can see that the keys vary from df to df
    #print(df2015["Country"])
    #print(df2015["Country"].isin(df2016["Country"]))
    #print(len(df2015.keys())) 12
    #print(len(df2016.keys())) 13
    #print(len(df2017.keys())) 12
    #
    


if __name__=="__main__":
    main()


