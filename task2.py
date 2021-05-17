from typing import List

from class_book import Book
from class_author import Author


class Library:
    def __init__(self, name: str, books=None, authors=None):
        self.authors = authors
        self.books = books
        self.name = name

    def new_book(self, name: str, year: int, author: Author):
        _book = Book(name, year, author)
        self.books.append(_book)
        return _book

    def group_by_author(self, author: Author):
        books_list = []
        for book in self.books:
            if author.__eq__(book.author):
                books_list.append(book)
        return books_list

    def group_by_year(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


"""
Task 2

Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and
adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
``
class Library:
    pass
class Book:
    pass
class Author:
    pass
```

"""
