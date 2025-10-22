
name = input("Enter your name: ")
year = int(input("Enter your year of birth: "))

def calculate_age(birth_year):
    current_year = 2025
    return current_year - birth_year
age = calculate_age(year)
print(f"Hello, {name}! You are {age} years old.")