# Завдання 3
#  До вже реалізованого класу «Автомобіль» додайте
# необхідні перевантажені методи та оператори.
class Car:
    def __init__(self, brand="", model="", year=0):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("Марка машини:", self.brand)
        print("Модель машини:", self.model)
        print("Рік:", self.year)

    def info(self):
        self.brand = input("Введіть марку машини:")
        self.model = input("Введіть модель машини:")
        self.year = int(input("Введіть рік:"))

    def __str__(self):
        return f"Машина: {self.brand}, Модель: {self.model}, Рік: {self.year}"

    def __eq__(self, other):
        return (self.brand, self.model, self.year) == (other.brand, other.model, other.year)

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

car1 = Car()
car1.info()

car2 = Car()
car2.info()

print("\nІнформація про першу машину:")
car1.display()

print("\nІнформація про другу машину:")
car2.display()

if car1 == car2:
    print("Машини однакові")
else:
    print("Машини різні")

if car1 < car2:
    print("Перша машина старіша")
else:
    print("Друга машина старіша")