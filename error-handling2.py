try:
  with open ('numbers.txt', 'r') as file:
    numbers = file.readlines()
    numbers = [float(num.strip()) for num in numbers]
    average = sum(numbers) / len(numbers)
    print(f"The average is: {average}")
except FileNotFoundError:
  print("Error: The file was not found.")
except ValueError:
  print("Error: The file contains non-numeric data.")
except Exception as e:
  print(f"An unexpected error occurred: {e}") 