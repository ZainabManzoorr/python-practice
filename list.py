books = ['The Great Gatsby', '1984', 'To Kill a Mockingbird', 'Pride and Prejudice']
books.append('1988')
print(books)
books.remove('1984')
print(books)
for book in books:
    print(book)
print(tuple(books))
