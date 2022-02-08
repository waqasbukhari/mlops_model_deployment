import pandas as pd

data_path = "/modified_census.csv"
data = pd.read_csv(data_path)
print(data.shape)
print(data.head())
print()
print(type(data))
print()
print("Salary column in modified_census.csv")
print("salary" in data.columns)
print(data.columns)
print()
