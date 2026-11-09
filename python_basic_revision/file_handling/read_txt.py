with open("data/students.txt","r") as file:
    content = file.read()
    print(content)



# Instead of reading entire file read line by line

with open("data/students.txt","r") as file:
    for line in file:
        print(line.strip())

