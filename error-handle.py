try:
  with open ('text.txt', 'r') as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("Error: The file was not found.")