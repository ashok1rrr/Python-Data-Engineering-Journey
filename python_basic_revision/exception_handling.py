# A. With try-except

# try:
#     file = open("students.json","r")
# except FileNotFoundError:
#     print("File not found")


# c.Multiple exceptions
try:
    a = int(input("Enter a num:"))
    b = int(input("Enter b numb:"))

    c = a/b
    print(c)

except ValueError:
    print("This is value error")
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print("Executed finally block")