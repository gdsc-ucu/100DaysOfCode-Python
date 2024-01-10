import pandas as pd 

df = pd.read_csv('dataset_file.csv')#original dataset

print("HEAD OF THE DATASET:")
print(df.head())

print("\nBUTTON ON DATASET:")
print(df.tail())

print("\nDESCRIPTIVE STATISTICS:")
print(df.describe())

print("\nCORRELATION MATRIX:")
print(df.corr())

print("\nCOUNTS OF UNIQUE VALUES:")
print(df.nunique())
