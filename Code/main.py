import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt
import readDat
import filePath
import os
def main():
    os.chdir(filePath.path["path"])
    # CSV file path here
    # You may need to change your path in the filePath.py file!
    path = filePath.path["path"]
    # Get the CSV files using readDat
    file_paths = readDat.glob_file(path)
    # read each csv into a pandas df
    readDat.read_data(file_paths)
    ###############################
    ###############################

if __name__=="__main__":
    main()
