# Sets

mySet = {1,2,3,4}
print(mySet)

# empty set
emptySet = {}

# Set with values of different datatypes
difSet = {'John',34,True,"ok"}

# Set of string items
stringSet = {'John','Kamal','Iddris'}

# set() - set constructor create a set
theSet = set(('J','K','L'))
print(theSet) # {'J', 'K', 'L'}

# Accessing the items of a set
ySet = {'Paul','Joe',True, 37}

for item in ySet:
    print(item)
 
 # Printing a specific item in a set
for item in ySet:
    if item == 'Joe':
        print(item)

if 'Joe' in ySet:
    print('Joe')

# add() - Adding an item to a set
x = { 1,2,4}
x.add(5)
print(x) # {1,2,4,5}

# remove() - Remove an item from a set
x.remove(2)
print(x) # {1,4,5}

# pop() - removes the last item from a set and returns it
print(x.pop()) # removes a random item that happens to be last
print(x) 

# update() - add items from on set to another
t = {'h','j','k'}
u = {'i','y','o'}
t.update(u)
print(t) # {'h','j','k','i','y','o'}

# items from any type of iterable can be added
v = ['l','g','w']
t.update(v) # {'h','j','k','i','y','o','l','g','w'}

# clear() - removes all the items in a set
u.clear() 
print(u) # {}

# union() - joins items from both sets 
a = {4,10,6,2}
b = {5,7,2,1}
t =  {8,9,10}
c = b.union(a,t) 
print(c) # {4,10,6,2,5,7,2,1}
print(a)

# intersection_update() - retains items present in both sets
r = {2,3,5}
s = {2,3,7}
r.intersection_update(s)
print(r)

# intersection() - creates a new set of the intersection of both sets 
v = {7,9,45}
w = {7,44,1}
vw = v.intersection(w)
print(vw)

# symmetric_difference() - create new set that keeps items that are not present in both sets
tr = {4,3,6,7}
ts = {4,3,5,8}

tx = tr.symmetric_difference(ts)
print(tx) #{5,6,7,8}

# symmetric_difference_update() - keeps items that are not present in both sets
ti = {1,2}
tq = {1,2,0}
#ti.symmetric_difference_update(tq)
print(ti) # 0
print(ti | tq) # union
print(ti & tq) # intersection
print(ti - tq) # difference
print(ti ^ tq) # symmetric difference

print(object(s), separator=separator, end=end, file=file, flush=flush)