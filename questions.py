def double_char(txt):
    word = ""
    for letter in txt:
        word += letter * 2
    return word

print(double_char("lllloooo"))        

def hamming_distance(txt1,txt2):
    ham = 0
    for item in range(len(txt1)):
        if txt1[item] != txt2[item]:
            ham += 1
    return ham

print(hamming_distance("thisisnice","niceisthis"))

# Dictionaries
myDict = {
    "name" : "Joel Agbe",
    "age"  : 45,
    "dob" : "03/03/1990",
    "married" : False,
    "gender" : "M",
    "height" : 1.70,
    "children" : ["Sylvester","Clinton","Martha"]
}

# Accessing a value in dictionary
print(myDict["name"])

# Accessing a value in a dictionary using get() 
print(myDict.get("dob"))

# Accessing the keys of a dictionary 
print(myDict.keys())

# Accessing the values of a dictionary
print(myDict.values())

#Printing the whole dictionary
print(myDict)

# Using the items() method changes dictionary into a list of tuples
print(myDict.items())

# checking for the existence of a value in dictionary
if "name" in myDict:
    print("it is there")

# Changing a value based on a key in a dictionary
myDict["age"] = 39
print(myDict["age"])

# update() - updates the dictionary of an existing key pair value
myDict.update({"married" : True})
print(myDict)

# pop() - removes and returns the key:value specified 
myDict.pop("name")
print(myDict)

#popitem() - removes and returns the last key:value pair
myDict.popitem()
print(myDict)