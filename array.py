array = [1, 2, 3, 4, 5]
for n in array:
    print(n)

array.append(6)
print("After appending 6:", array)

array.pop()
print("After popping:", array)

array.insert(2, 10)
print("After inserting 10 at index 2:", array)

size = 5
array2 = [1] * size
print("Array of size 5 with all elements as 1:", array2)

print(array[-1])
print(array[-2])

print("Sliced array (index 1 to 4):", array[1:5])
print("Sliced array (start to index 3):", array[:4])
print("Sliced array (index 2 to end):", array[2:])

#unpacking
a, b, c, d, e = [1,2,3,4,5]
print("Unpacked values:", a, b, c, d, e)

#loop through array
nums = [10, 20, 30, 40, 50]

#without index
for num in nums:
    print("Number:", num)
    
#with index
for i in range(len(nums)):
    print("Index:", i, "Number:", nums[i])
    
#using enumerate
for index, value in enumerate(nums):
    print("Index:", index, "Value:", value)

#loop through multiple arrays simultaneously
array2 = [1, 2, 3]
array3 = ['a', 'b', 'c']
for num, char in zip(array2, array3):
    print("Number:", num, "Character:", char)

#reverse array
array.reverse()
print("Reversed array:", array)

#sort array (Ascending)
array.sort()
print("Sorted array:", array)

#sort array (Descending)
array.sort(reverse=True)
print("Sorted array (Descending):", array)

#sort
array4 =['banana', 'apple', 'cherry', 'date']
array4.sort()
print("Sorted array of strings:", array4)

#custom sort (by length of string)
array4.sort(key=lambda x: len(x))
print("Custom sorted array by length:", array4)