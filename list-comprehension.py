numbers : list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers : list[int] = [pow(number,2) for number in numbers if number % 2 == 0]
print(squared_numbers)
