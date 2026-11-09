import csv

with open("data/students.csv", "r") as file:

    reader = csv.reader(file)

    for line in reader:

        print(line)

with open("data/students.csv","r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])

# Find students who scored more than 80 marks.
with open("data/students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = int(row["marks"])

        if marks > 80:
            print(row["name"],marks)



