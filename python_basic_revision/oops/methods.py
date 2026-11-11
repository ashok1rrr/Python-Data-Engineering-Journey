class Student:
    def __init__(self,name,age,gender,rollnumber):
        self.name = name
        self.age = age
        self.gender = gender
        self.rollnumber = rollnumber

    def display(self):
        print("name",self.name)
        print("name",self.age)
        print("name",self.gender)
        print("name",self.rollnumber)

    def gender_check(self):
        if self.gender == "Male":
            print("This gender is Male")
        else:
            print("Other")

student1 = Student("Ashok",22,"Maghle",1)
student1.display()
student1.gender_check()