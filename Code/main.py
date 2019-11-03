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
    try:
        df2015 = readDat.csv_to_dataframe(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2015.csv")
        df2016 = readDat.csv_to_dataframe(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2016.csv")
        df2017 = readDat.csv_to_dataframe(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2017.csv")
    except:
        print("Failed to read a csv file to pandas dataframe!")
    ###############################
    ###############################

if __name__=="__main__":
    main()