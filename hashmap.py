#Hashmap aka dictinary in Python
myhashmap = {}
myhashmap["name"] = "Alice"
myhashmap["age"] = 30
print("Hashmap:", myhashmap)
print(len(myhashmap))

myhashmap["age"] = 31  # Update age
print("Updated Hashmap:", myhashmap)

myhashmap.pop("name")
print("After removing name:", myhashmap)

#dictionary comprehension
squared = {x: x*x for x in range(5)}
print("Squared dictionary:", squared)

#loop through hashmap
for key in myhashmap:
    print("Key:", key, "Value:", myhashmap[key])

for val in myhashmap.values():
    print("Value:", val)

for key in myhashmap.keys():
    print("Key:", key)
    
for key, value in myhashmap.items():
    print("Key:", key, "Value:", value)