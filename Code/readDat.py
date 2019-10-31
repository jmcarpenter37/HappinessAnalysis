import pandas as pd
import glob
import numpy as np
# Use glob to get the realtive paths of the csv files
def glob_file(path_to_csv):
    files = glob.glob1(path_to_csv , "*.csv")
    return files
# Read data into pandas dataframe function
def read_data(data_file_list):
    for file in range(len(data_file_list)):
        df = pd.read_csv(r"{}".format(file))
        print(df)

