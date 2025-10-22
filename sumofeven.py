num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
def sum_of_evens(n1, n2):
  if n1 % 2 == 0 and n2 % 2 == 0:
    return n1 + n2
  else:
    return "Both numbers must be even."
result = sum_of_evens(int(num1), int(num2))
print("The sum is:", result)