class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def input_data(self):
        self.name = input("Введите название страны: ")
        self.continent = input("Введите название континента: ")
        self.population = int(input("Введите количество жителей в стране: "))
        self.phone_code = input("Введите телефонный код страны: ")
        self.capital = input("Введите название столицы: ")
        self.cities = input("Введите названия городов через запятую: ").split(', ')

    def display_data(self):
        print(f"Название страны: {self.name}")
        print(f"Название континента: {self.continent}")
        print(f"Количество жителей: {self.population}")
        print(f"Телефонный код страны: {self.phone_code}")
        print(f"Столица: {self.capital}")
        print(f"Города: {', '.join(self.cities)}")

    def get_name(self):
        return self.name

    def get_continent(self):
        return self.continent

    def get_population(self):
        return self.population

    def get_phone_code(self):
        return self.phone_code

    def get_capital(self):
        return self.capital

    def get_cities(self):
        return self.cities

    def set_name(self, name):
        self.name = name

    def set_continent(self, continent):
        self.continent = continent

    def set_population(self, population):
        self.population = population

    def set_phone_code(self, phone_code):
        self.phone_code = phone_code

    def set_capital(self, capital):
        self.capital = capital

    def set_cities(self, cities):
        self.cities = cities

cities = ["Кривой Рог", "Днепр", "Киев", "Львов"]
country1 = Country("Украина", "Евразия", 40005183, "+380", "Киев", cities)
country1.display_data()

country1.set_population(30795098)
print(f"Новое количество жителей в Украине: {country1.get_population()}")
