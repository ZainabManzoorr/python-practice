##with open('text.txt', 'r') as file:
##content = file.read()
##print(content)
with open('text.txt', 'w') as file:
    file.write("This is a new line added to the file.\n")
    file.writelines(["First line.\n", "Second line.\n", "Third line.\n"])
with open('text.txt', 'a') as file:
    file.write("Appending new content!\n")
