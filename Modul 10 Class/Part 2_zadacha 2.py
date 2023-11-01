class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"Название: {self.title}, Год выпуска: {self.year}, Издатель: {self.publisher}, Жанр: {self.genre}, Автор: {self.author}, Цена: ${self.price:.2f}"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def input_data(self):
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(self)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

book1 = Book("Преступление и наказание", 1866, "Вестник", "Роман", "Достоевский", 40.00)
book2 = Book("Гарри Поттер", 2000, "Вести", "Роман", "Дж. Роулинг", 50.00)

print(book1)
print(book2)

if book1 == book2:
    print("Цены равны")
elif book1 < book2:
    print("Книга 1 дешевле")
else:
    print("Книга 2 дешевле")
