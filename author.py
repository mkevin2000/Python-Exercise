class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author

my_book = Book("Python Basics", 350, "Alex Lee")

print(my_book.author)