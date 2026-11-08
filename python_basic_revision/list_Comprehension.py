# List comprehension is a shorter way to create a new list from an existing iterable, optionally applying conditions.



# Normal for loop

numbers = [1,2,3,4,5]
sq = []

for n in numbers:
    sq.append(n**2)
print(sq)


# Using list comprehension
# The same operation can be written in one line:

# Syntax
# new_list = [expression for item in iterable]

numbrs = [1,2,3,4,5,6,7]
squr = [nn ** 2 for nn in numbrs]
print(squr)



students = [
    {"name": "Arjun", "age": 20},
    {"name": "Ravi", "age": 18},
    {"name": "Kiran", "age": 21}
]

students_names = [student["name"] for student in students]
print(students_names)