students = [
    "Arjun",
    "Ravi",
    "Kiran",
    "Sai"
]

with open("data/output.txt","w") as file:
    for student in students:
        file.write(student + "\n")
print("File created successfully")


with open("data/output.txt","a") as file1:
    file1.write("Ashok")
print("New student Added")