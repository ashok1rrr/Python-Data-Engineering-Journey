import pandas as pd

data = {
    "name" : ["Aravind", "Ashok", "Charan"],
    "Age" : [23,24,25],
    "city" : ["Hyd","Banglr","Chennei"]
}

df = pd.DataFrame(data)
print(df)