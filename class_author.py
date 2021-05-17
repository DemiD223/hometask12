# from class_book import Book
# from typing import List


class Author:
    def __init__(self, name: str, country: str, birthday: str, books):
        self.books = books
        self.birthday = birthday
        self.country = country
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.birthday == other.birthday
        return False

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday} {self.books}'

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday} {self.books}'
