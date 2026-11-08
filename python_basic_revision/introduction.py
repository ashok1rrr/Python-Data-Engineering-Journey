# Variables:
name = 'Ashok'
age = 21
gender = 'Male'
salary = 2.8

print(name)
print(age)
print(gender)
print(salary)


# Data Types
# int, float, str, bool, list, tuple, dict, set, NoneType

print(type(name))

# Type conversion
# Converting one datatype to another is called type casting

print('before converting to:',type(age))
age = str(age)
print('after converting to:',type(age))

# Lists, Tuples, Dictionaries and Sets
# --> These are called python collection data types, They allow to store multiple values into a single variable

# A. List
# A list is a ordered and mutable collection that allows duplicates

students = ['Lovely','Pathala','Bete','Pathala','m']
print('These are list datatype output:',students)

# Important list operations are:

# Access element
print(students[-5])
# Add element
students.append('Rakesh')
# Insert element
students.insert(2,'Bhanu')
# Remove element
students.remove('Pathala')
# Update element
students[0] = 'lovelamma'

print('These are list datatype output:',students)

# B.Tuple
# A tuple is an ordered and immutable allows duplicates
employee = ('Arjun',30,"Tirupati")
print("Before operations on tuple:",employee)

print(employee[2])
# employee[0] = 'Ashok'     tuple Don't allow assignment


# C.Dictionary
# A dictionary store data in key value pairs

student = {
    "id":101,
    "name":"Puppy",
    "age":14,
    "city":"Hyderabad"
}
print(student)

print('Hi',student["name"])

# Important operations on dictionary
# Add new Key
student["Aadhar"] = 8978

# Update value
student["age"] = 16

# Remove key
student.pop("city")

print('Get Keys',student.keys())
print('Get values',student.values())

# Get key value pairs
print('Normal',student)
print('item function',student.items())


# D. SET
# Set is a unordered collection automatically removes the duplicates

num = {1,1,3,4,55,2,1}
print(num)

# Important set operations
numbers = {10,20,30}

# Add element
numbers.add(40)

# Remove element
numbers.remove(10)

print(numbers)

unique_nums = set(num)
print(unique_nums)


# Else if Statements
# if statement
m = 20

if m >=35:
    print("Hi ra bondam.. Kanna reyy")
else:
    print("Fail")



# For and While loops

s = ["Ashok",12,4,"Guru"]
for student in s:
    print(student)

for i in range(1,5):
    print(s[0])



# Calculate the total marks
markss = [1,2,3,4,5,6,7]
total = 0

for i in markss:
    total = total + i

print(total)

# While Loop
count = 1

while count <= 5:
    print(count)

    count = count+1


# C. Break and Continue
# Break : Terminates the loop immediatly
for i in range(1,20):
    if i == 3:
        break

    print('This is break related:',i)

# Continue : Terminates the loop immediatly
for i in range(1, 10):
    if i == 2:
        continue
    print('This is continue related',i)


