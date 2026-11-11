# Inheritance allows one class reuse the properties and methods to another class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name : ",self.name)
        print("Age :",self.age)

class Student(Person):
    def study(self):
        print(self.name, "is studying")


class Teacher(Person):
    def teach(self):
        print(self.name, "is Teaching")

student1 = Student("Ashok",25)
teacher1 = Teacher("Guru",24)

student1.study()