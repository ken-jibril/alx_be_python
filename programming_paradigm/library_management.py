class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private availability attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store books

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # book not found or unavailable

    def return_book(self, title):
        """Return a book and make it available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # book not found or not checked out

    def list_available_books(self):
        """Print titles and authors of all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
