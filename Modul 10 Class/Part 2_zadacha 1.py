class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def __str__(self):
        return f"Модель: {self.model}, Год выпуска: {self.year}, Производитель: {self.manufacturer}, Объем двигателя: {self.engine_capacity} л, Цвет: {self.color}, Цена: ${self.price:.2f}"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_capacity = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(self)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

car1 = Car("BMW X5", 2021, "BMW", 2.5, "Черный", 30000.0)
car2 = Car("Shkoda Fabia", 2019, "Shkoda", 2.3, "Белый", 20000.0)

print(car1)
print(car2)

if car1 == car2:
    print("Цены равны")
elif car1 < car2:
    print("Автомобиль 1 дешевле")
else:
    print("Автомобиль 2 дешевле")
