import json

with open("data/students.json","r",newline="") as file:
    r = json.load(file)

print(r)


# Access specific values
with open("data/students.json","r",newline="") as file:
    data = json.load(file)

print("school:",data["school"])

for student in data["students"]:
    print(student["name"])
    print(student["course"])