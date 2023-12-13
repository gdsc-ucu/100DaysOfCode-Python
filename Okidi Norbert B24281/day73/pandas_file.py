import pandas as pd 

df = pd.read_csv('dataset_file.csv')#original dataset
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
#cleaned dataset
print(df.info())