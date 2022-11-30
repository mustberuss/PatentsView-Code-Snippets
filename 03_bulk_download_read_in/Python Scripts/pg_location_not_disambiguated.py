#Read-in script for Number of figures and sheets

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
import numpy as np

# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")

file_name = "pg_location_not_disambiguated.tsv.zip"
f_name = "pg_location_not_disambiguated.tsv"
# Selecting the zip file.
with zip.ZipFile(file_name) as zf:
    chunksize = 15*(10 ** 5)
    count = 1
    n_obs = 0
    dtype={'sequence': int}
    for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize, quoting= csv.QUOTE_NONNUMERIC):
        print('processing chunk: ' + str(count))
        n_obs += len(df)
        count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)
print(df.describe(exclude=[np.number]))
