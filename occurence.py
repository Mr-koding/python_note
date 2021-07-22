def find_odd(lst):
    for val in lst:
        if lst.count(val) % 2 == 1:
            return val

a = [1,2,3,1,1,2,3]
print(find_odd(a))

# multidimensional lists

multi = [
             [3,64], [346,747,34], [3,63], [36,653]
        ]

# Accessing the items of a multidimensional list
print(multi[2][1]) # 63
print(multi[2]) # [3, 63]

# tuple

myTuple = (23,54,6345,4)

# empty tuple
emptyTuple = ()

# tuple of values of different datatypes
difTuple = ('Mike', 26, True)

# tuple of lists
tupleList = ([34,True],['gone',45.4],['J'])

# tuple of tuples/nested tuple
tupleOfTuple = ((45.8,4),(True, 'Money'))

# tuple packing
valTuple = 34, 56, 48, 67
print(valTuple)

# tuple unpacking
firstVal, secVal, thirdVal, fourVal = valTuple

print(firstVal,secVal,thirdVal,fourVal)
print(fourVal)

# tuple unpacking by using less variables
f, s, *t = valTuple
print(f,s,t)
# 34, 56, [48, 67] 

# count() - counting the occurence of a specific item in a tuple
print(valTuple.count(34)) # 1

# index() - finding the index of an item
print(valTuple.index(34)) # 0

# Tuple concatenation
first = ('a', 'b', 'c')
sec = ('d','e', 'f')
third = first + sec
print(third) 

# tuple repetition
print(first * 3)

first[-1]
first[1:]

# deleting the tuple completely
del first
print(first) # not defined

