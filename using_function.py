# User-defined functions

#Defining the function
def myFirstFunction():
    print("Hi class")

# Calling the function
myFirstFunction()

# Creating a function that returns a value
def greetings(name):
    return "Hello " + name  
print(greetings("John"))

# Creating a function that takes more than on parameter
def fullName(first,last):
    return first +" "+ last

print(fullName("Kwame","Nkrumah"))

# Create a function that takes two numbers as parameters, adds them and returns the sum
def sum(num1,num2):
    return num1 + num2
print(sum(34,56.5))
    
# Write a function that takes a list as a parameter, reverses the list and removes the last item of the list. return the list at the end 
def changeList(lst): # hint
    lst.reverse() # this is to reverse the list
    lst.pop() # this is to remove the last item from the list 
    return lst # this returns the list

print(changeList([23,3,6,4,7,5,45]))

# Using variable inside a function
def mainFunction(firstname,lastname):
    #lastname = "Boateng"
    return firstname + " " + lastname

print(mainFunction("Paul", "Nkrumah"))

mainFunction("mawuli")




