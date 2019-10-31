import pandas as pd
import glob
# Use glob to get the realtive paths of the csv files

# Read data into pandas dataframe function
def read_data(data_path):
    df = pd.read_csv(r"{}".format(data_path))
    return df

