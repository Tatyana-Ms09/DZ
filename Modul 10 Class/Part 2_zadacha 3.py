class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Название стадиона: {self.name}\nДата открытия: {self.opening_date}\nСтрана: {self.country}\nГород: {self.city}\nВместимость: {self.capacity} человек"

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def display_data(self):
        print(self)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self, name):
        self.name = name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

# Пример использования класса:
stadium1 = Stadium("Спартак", "19 мая 2020", "Украина", "Кривой Рог", 5000)
stadium2 = Stadium("Олимп", "01 июня 2010", "Украина", "Киев", 35000)

print("Стадион 1:")
stadium1.display_data()

print("\nСтадион 2:")
stadium2.display_data()

if stadium1 == stadium2:
    print("Вместимость стадионов равна")
elif stadium1 < stadium2:
    print("Стадион 1 вмещает меньше зрителей")
else:
    print("Стадион 2 вмещает меньше зрителей")
