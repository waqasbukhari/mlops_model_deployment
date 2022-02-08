import os
import pandas as pd

data_path = os.path.join(os.getcwd(), r"modified_census.csv")
print(os.getcwd())
print()
data = pd.read_csv(data_path)
print(data)
print()
print(data.shape)
print(data.head())
print()
print(type(data))
print()
print("Salary column in modified_census.csv")
print("salary" in data.columns)
print(data.columns)
print()
