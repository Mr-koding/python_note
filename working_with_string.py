# String formatting/manipulation

# String is an array of characters/object
# A string an immutable sequence of characters

myString = "this is a string"
"this 23 is also string"
"344"
""
"   "
"True"
'I can have single quote'
"@#$%#$%&^"
"[34,34,56]"

# Strings have indices
print(myString[2]) # i

# Slicing can be performed on a string
print(myString[2:8])

# String interpolation
name = "George"
print(f"My name is {name}")

# String formatting
firstname = "Joel"
age = 30
gender = "Male"
print("{1} is a {0} of {2} years old".format(firstname,gender,age))

# Named indexes
mes = "I have a very nice {house}".format(house = "Palace house")
print(mes)

#String concatenation 
val1 = "i"
val2 = "phone"
val3 = "x"

full = val1 + val2 + " " + val3
print(full)

print(f"{val1}{val2} {val3}")
