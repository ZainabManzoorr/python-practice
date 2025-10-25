#tuples are like arrays but they are immutable
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(tuple1[0])
print(tuple1[-1])
print(len(tuple1))
#tuple1[0] = 10 # This will raise an error because tuples are immutable

#can be used as keys in dictionaries
tuple_dict = {
    (1, 2): "a",
    (3, 4): "b"
}
print(tuple_dict[(1, 2)])
