mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(2)  # Duplicate, will not be added
print(mySet)
print(len(mySet))
print(1 in mySet)
print(3 in mySet)
mySet.remove(2)
print(mySet)

print(set([1, 2, 3, 4, 5]))
set = {i for i in range(5)}
print(set)