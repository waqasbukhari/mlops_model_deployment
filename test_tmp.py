import pandas as pd

data_path = "modified_census.csv"
data = pd.read_csv(data_path)
print("Salary column in modified_census.csv")
print("salary" in data.columns)
print(data.columns)
print()
