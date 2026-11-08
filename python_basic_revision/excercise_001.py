# How all four concepts work together in Data Engineering
# Let's consider a practical example.

# You receive student records from an API and want to identify valid students.


students = [
    {"name": "Arjun", "age": 20, "marks": 85},
    {"name": "Ravi", "age": 17, "marks": 90},
    {"name": "Kiran", "age": 22, "marks": 75},
    {"name": "Sai", "age": 15, "marks": 30}
]

valid_students = []

for student in students:
    if student["age"] >= 18 and student["marks"]>=35:
        valid_students.append(student)
print('Valid students:',valid_students)

