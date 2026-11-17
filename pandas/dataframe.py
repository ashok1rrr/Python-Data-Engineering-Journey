# A data frame is a two dimentional data structure consisting rows and columns
# Its a similar of excel sheets or database model

import pandas as pd

data = {
    "Employee_ID": [101, 102, 103],
    "Name": ["Aravind", "Rahul", "Priya"],
    "Salary": [25000, 30000, 35000],
    "Department": ["IT", "HR", "Finance"]
}

df = pd.DataFrame(data)
print(df)


# Creating from a list 
data = [
    ["Aravind",23,"Hyd"],
    ["Ashok",21,"chennai"],
    ["Charan",22,"Bnglr"]
]

df = pd.DataFrame(data, columns=["Name","Age","City"])
print(df)