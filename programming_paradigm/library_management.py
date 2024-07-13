# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
   


# library_management.py

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book.title} by {book.author}")
                else:
                    print(f"{book.title} is already checked out.")
                return
        print(f"Book not found: {title}")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book.title} by {book.author}")
                else:
                    print(f"{book.title} is already available.")
                return
        print(f"Book not found: {title}")

    def list_available_books(self):
        if not self._books:
            print("No books available.")
        else:
            print("Available books:")
            for book in self._books:
                if not book._is_checked_out:
                    print(f"{book.title} by {book.author}")

