# String Manipulation
# A string is a sequence of characters enclosed with single,double or triple quotes

name = "Ashok"
print(name)

# A. Convert upper case and lower case
print(name.upper())
print(name.lower())
print(name.title())


# B. Remove unneccessary spaces
name_one = "       hey...Gd Mrng..              "

print("using strip function: ",name_one.strip())
print("using lstrip function:",name_one.lstrip())
print("using rtrip function:", name_one.rstrip())

print(name_one)

# c. Replace characters
text  = "I am a Data engineer"

new_text = text.replace("engineer","scientist")
print(new_text)


# D. Split a String into a list

data = "Ashok, Bhanu, Lovely, Anjali, Navya, Yash, Bete"
employees = data.split("ve")
print(employees)


# Join strings
stude = ["Ashok", "Bhanu", "Lovely"]
std = ": ".join(stude)
print(stude)


# Find and check text
email = "rguruashok@gmail.com"

print(email.find("@"))
print(email.startswith("rgu"))
print(email.endswith("com"))

# String formatting (f-strings)

nm = "Ashok"
age = 23

message = f"{nm} is a handsome and age is {age}"
print(message)


