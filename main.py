# Завдання 4
# До вже реалізованого класу «Книга» додайте
# необхідні перевантажені методи та оператори.

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def information(self):
        print(f"Назва: {self.title},\nАвтор: {self.author},\nЖанр: {self.genre}")

    def __eq__(self, other):
        return (self.title, self.author, self.genre) == (other.title, other.author, other.genre)

    def __lt__(self, other):
        return (self.title, self.author) < (other.title, other.author)

    def __gt__(self, other):
        return (self.title, self.author) > (other.title, other.author)

    def __str__(self):
        return f"Книга {self.title} автора {self.author} та жанр: {self.genre}"


book1 = Book("12 правил життя", "Джордана Пітерсон", "допоможи собі сам")
book2 = Book("48 законів влади", "Роберт Грін", "нон-фікшн")

if book1 > book2:
    print(f"Книга '{book1.title}' автора {book1.author} знаходиться в алфавітному порядку вище '{book2.title}' автора {book2.author}")
else:
    print(f"Книга '{book2.title}' автора {book2.author} знаходиться в алфавітному порядку вище '{book1.title}' автора {book1.author}")

if book1 == book2:
    print("Книги однакові")
else:
    print("Книги різні")