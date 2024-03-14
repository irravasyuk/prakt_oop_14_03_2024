# Завдання 2
#  Реалізуйте клас «Стадіон». Збережіть у класі: назву
# стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій. До вже реалізованого класу «Стадіон» додайте
# необхідні перевантажені методи та оператори.
class Stadium:
    def __init__(self, name="", date="", country="", city="", capacity=0):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display(self):
        print("Назва стадіону:", self.name)
        print("Дата відкриття:", self.date)
        print("Країна:", self.country)
        print("Місто:", self.city)
        print("Місткість:", self.capacity)

    def info(self):
        self.name = input("Введіть назву стадіону:")
        self.date = input("Введіть дату відкриття стадіону:")
        self.country = input("Введіть назву країни:")
        self.city = input("Введіть місто:")
        self.capacity = int(input("Введіть місткість стадіону:"))

    def __str__(self):
        return f"Стадіон {self.name}, Дата відкриття: {self.date}, Знаходиться {self.country}, {self.city}, Місткість стадіону: {self.capacity}"

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __ne__(self, other):
        return self.capacity != other.capacity

stadium1 = Stadium()
stadium1.info()

stadium2 = Stadium()
stadium2.info()

print("\nІнформація про перший стадіон:")
stadium1.display()

print("\nІнформація про другий стадіон:")
stadium2.display()

if stadium1 >= stadium2:
    print("\nПерший стадіон має більшу місткість, ніж другий")
else:
    print("\nДругий стадіон має більшу місткість, ніж перший")

