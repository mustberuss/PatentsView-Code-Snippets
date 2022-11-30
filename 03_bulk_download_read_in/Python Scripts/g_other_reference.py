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

file_name = "g_other_reference.tsv.zip"
f_name = "g_other_reference.tsv"
# Selecting the zip file.
with zip.ZipFile(file_name) as zf:
# Reading the selected file in the zip.
    with zf.open(f_name) as openfile: 
        df = pd.read_csv(openfile, delimiter="\t", quoting = csv.QUOTE_NONNUMERIC)

chunksize = 15*(10 ** 5)
count = 1
n_obs = 0
dtype={'sequence': int}
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)
print(df.describe(exclude=[np.number]))
