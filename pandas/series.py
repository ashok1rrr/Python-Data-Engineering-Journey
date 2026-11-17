# A Series is a one dimentional labeled array
# Its represents single column of data

import pandas as pd

salaries = pd.Series([10000,20000,30000,35000,40000])
print(salaries)

print(salaries[2])


# Giving custom indexes

salary = pd.Series(
    [25000,30000,35000],index=["A","B","C"]
)
print(salary["A"])