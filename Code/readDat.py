import pandas as pd
import glob
import numpy as np
# Use glob to get the realtive paths of the csv files
def glob_file(path_to_csv):
    files = glob.glob1(path_to_csv , "*.csv")
    return files
# Read data into pandas dataframe function
def csv_to_dataframe(file_path):
    try:
        df = pd.read_csv(file_path)
    except NotADirectoryError as err:
        print("That's not a directory on this machine.")
    return df

















