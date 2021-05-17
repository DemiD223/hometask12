from task2 import Library, Book, Author
from task1 import Dog, Cat, animal_talk
from task3 import Fraction

if __name__ == '__main__':
    # Task 1
    animal_talk(Cat())
    animal_talk(Dog())
    # Task 2
    orwell = Author('George Orwell', 'British India', '1903.06.25', [])
    doyle = Author('Arthur Conan Doyle', "Great Britain", '1859.05.22', [])
    warner = Author('Jack Warner Schaefer', 'USA', '1907.11.19', [])
    book1 = Book('1984', 1949, orwell)
    book2 = Book('Animal Farm: A Fairy Story', 1945, orwell)

    l1 = Library("first city library", [book1, book2, Book('Homage to Catalonia', 1938, orwell)],
                 [orwell, ])
    l1.new_book('Burmese Days', 1934, orwell)
    l1.new_book('A Scandal in Bohemia', 1891, doyle)
    l1.new_book('Shane', 1949, warner)
    list_by_author = l1.group_by_author(Author('George Orwell', 'British India', '1903.06.25', []))
    print(list_by_author)
    list_by_date = l1.group_by_year(1949)
    print(list_by_date)
    # Task 3
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
