import json

student = {
    "id": 104,
    "name": "Sai",
    "age": 22,
    "course": "Java"
}

with open("data/output.json","w") as file:
    json.dump(student,file,indent=4)

print("JSON file created successfully")