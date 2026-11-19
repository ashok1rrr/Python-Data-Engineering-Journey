import pandas as pd

df = pd.read_csv("employees.csv")
print(df)

# Reading specific number of rows

df = pd.read_csv("employees.csv", nrows=2)
print(df)


# Reading columns from specific columns
df = pd.read_csv("employees.csv", usecols=["Name","Salary"])
print(df)