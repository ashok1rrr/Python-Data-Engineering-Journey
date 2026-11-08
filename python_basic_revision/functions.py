# 1. Functions

# Functions is a block of code which can be reuse instead of writing duplicate

# A. Creating a function
def greet():
    print("Welcome to python")
greet()

# B. Function with parameters
def greetp(name):
    print("Hello", name)
greetp("Ashok")
greetp("Ayush")


# C. Function with return
def add(a,b):
    result = a+b
    return result

result = add(1,3)
print(result)

# D. Default parameters
def greetd(name = 'student'):
    print("Hello",name)

greetd(1)

# Multiple return values
def calculate(a,b):
    return a+b,a-b,a*b,a/b

addition, substraction, multiplication, division = calculate(3,5)
print(addition)



# Real-world Example:
# Imagine receive student records and need to validate each record.

def validate_students(studunt):
    if studunt["age"] > 18 and studunt["marks"] >= 35:
        return True
    return False

studunt = {
    "name" : "Ashok",
    "age":2,
    "marks": 36
}

sf = validate_students(studunt)
print(sf)