import pandas as pd

dataset1 = pd.read_csv("data/data_main.csv")     # Dataset1 is the main data

# Dataset2 is the data you want to add
dataset2 = pd.read_csv("month2_data.csv")        # Change the path to add month3_data.csv 

# Append rows of dataset2 to dataset1
dataset1 = pd.concat([dataset1, dataset2],axis=0, ignore_index=True)

# Overwrite data_main.csv file
dataset1.to_csv("data/data_main.csv", index=False) 
