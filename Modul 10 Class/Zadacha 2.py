class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        self.name = input("Введите название города: ")
        self.region = input("Введите название региона: ")
        self.country = input("Введите название страны: ")
        self.population = int(input("Введите количество жителей в городе: "))
        self.postal_code = input("Введите почтовый индекс города: ")
        self.phone_code = input("Введите телефонный код города: ")

    def display_data(self):
        print(f"Название города: {self.name}")
        print(f"Название региона: {self.region}")
        print(f"Название страны: {self.country}")
        print(f"Количество жителей: {self.population}")
        print(f"Почтовый индекс: {self.postal_code}")
        print(f"Телефонный код: {self.phone_code}")

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_country(self):
        return self.country

    def get_population(self):
        return self.population

    def get_postal_code(self):
        return self.postal_code

    def get_phone_code(self):
        return self.phone_code

    def set_name(self, name):
        self.name = name

    def set_region(self, region):
        self.region = region

    def set_country(self, country):
        self.country = country

    def set_population(self, population):
        self.population = population

    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def set_phone_code(self, phone_code):
        self.phone_code = phone_code

city1 = City("Кривой Рог", "Днепропетровская область", "Украина", 418079, "50065", "+380")
city1.display_data()

city1.set_population(455000)
print(f"Новое количество жителей: {city1.get_population()}")
