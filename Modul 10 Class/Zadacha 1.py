class Person:
    def __init__(self, full_name, birthdate, phone_number, city, country, address):
        self.full_name = full_name
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        self.full_name = input("Введите ФИО: ")
        self.birthdate = input("Введите дату рождения: ")
        self.phone_number = input("Введите контактный телефон: ")
        self.city = input("Введите город: ")
        self.country = input("Введите страну: ")
        self.address = input("Введите домашний адрес: ")

    def display_data(self):
        print(f"ФИО: {self.full_name}")
        print(f"Дата рождения: {self.birthdate}")
        print(f"Контактный телефон: {self.phone_number}")
        print(f"Город: {self.city}")
        print(f"Страна: {self.country}")
        print(f"Домашний адрес: {self.address}")

    def get_full_name(self):
        return self.full_name

    def get_birthdate(self):
        return self.birthdate

    def get_phone_number(self):
        return self.phone_number

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_address(self):
        return self.address

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.country = country

    def set_address(self, address):
        self.address = address

person1 = Person("Присяжнюк Татьяна Николаевна", "11.09.1996", "+380 (96) 999 99 99", "Кривой Рог", "Украина", "ул. Ленина, д. 111")
person1.display_data()

person1.set_phone_number("+380 (98) 555 55 55")
print(f"Новый контактный телефон: {person1.get_phone_number()}")
