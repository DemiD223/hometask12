# from class_author import Author


class Book:
    count_books = 0

    def __init__(self, name: str, year: int, author):
        Book.count_books += 1
        self.author = author
        self.year = year
        self.name = name

    def __repr__(self):
        return f"Name: {self.name} Year: {self.year} Author: {self.author.name}"

    def __str__(self):
        return f"{self.name} {self.year} {self.author.name}"
