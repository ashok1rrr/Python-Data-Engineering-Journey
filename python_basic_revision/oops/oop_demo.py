class Student:
    name = "Ashok.r"
    age = 20

student1 = Student()
# print(student1.name)
# print(student1.age)
stu2 = Student()
stu2.sdhj = "kj"
print(stu2.sdhj)



# Create Multiple objects
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()


emp1.name = "Ashok"
emp1.age = 23

print(emp1.name)

# Constructor
# Constructor is a initilization mechanism that runs automatically when we create object

# __init__() is the initializer method

# Instead of assigning details saparatly , we have pass them while creating objects

class Student1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

stud1 = Student1("Akash",33)
print(stud1.name,stud1.age)
