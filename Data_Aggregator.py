import pandas as pd

# Assume dataset1 and dataset2 are already loaded as pandas DataFrames
# dataset1 is the main data, and dataset2 is the data you want to add

dataset1 = pd.read_csv("data/Data_Main.csv")  # Example loading dataset1
dataset2 = pd.read_csv("Month3.csv")  # Example loading dataset2

# Append rows of dataset2 to dataset1
dataset1 = pd.concat([dataset1, dataset2],axis=0, ignore_index=True)

dataset1.to_csv("data/Data_Main.csv", index=False) 
