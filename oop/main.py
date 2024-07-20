from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()


from main import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_main = Library()

    # Create instances of each type of book
    classic_book = Book("Book: Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("EBook: Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("PrintBook: The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_main.add_book(classic_book)
    my_main.add_book(digital_novel)
    my_main.add_book(paper_novel)

    # List all books in the library
    my_main.list_book()

if __name__ == "__main__":
    main()