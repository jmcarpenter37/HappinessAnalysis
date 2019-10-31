import pandas as pd
import glob

# Use glob to get the realtive paths of the csv files
def glob_file(path_to_csv):
    files = glob.glob1(path_to_csv , "*.csv")
    return files
# Read data into pandas dataframe function
def read_data(data_path):
    df = pd.read_csv(r"{}".format(data_path))
    return df

