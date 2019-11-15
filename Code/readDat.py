import pandas as pd
# Read data into pandas dataframe function
def csv_to_dataframe(file_path):
    try:
        df = pd.read_csv(file_path)
    except NotADirectoryError as err:
        print("That's not a directory on this machine.")
    return df

















