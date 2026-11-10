import csv

python_students = [
    {"id":101,"name":"Arjun","course":"Python"},
    {"id":102,"name":"kiran","course":"Python"}
]

with open("data/python_student.csv","w",newline="") as file:
    fieldnames = ["id","name","course"]

    writer = csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(python_students)


print("CSV File created successfully")
