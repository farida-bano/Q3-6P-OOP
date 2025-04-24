# 11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0  # Class-level variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Test the class method
book1 = Book()
book2 = Book()
book3 = Book()

# Call the class method for each book to increment the total book count
book1.increment_book_count()
book2.increment_book_count()
book3.increment_book_count()

# Print the total book count
print(f'Total books: {Book.total_books}')
