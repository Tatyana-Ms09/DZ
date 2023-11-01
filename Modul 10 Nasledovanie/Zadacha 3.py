class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars = dollars
        self.cents = cents

    def display(self):
        print(f"Сумма: {self.dollars} долларов и {self.cents} центов")

    def set_dollars(self, dollars):
        self.dollars = dollars

    def set_cents(self, cents):
        self.cents = cents

    def add(self, other_money):
        total_dollars = self.dollars + other_money.dollars
        total_cents = self.cents + other_money.cents

        if total_cents >= 100:
            total_dollars += total_cents // 100
            total_cents %= 100

        return Money(total_dollars, total_cents)

    def subtract(self, other_money):
        total_dollars = self.dollars - other_money.dollars
        total_cents = self.cents - other_money.cents

        if total_cents < 0:
            total_dollars -= 1
            total_cents += 100

        return Money(total_dollars, total_cents)

# Пример использования класса:
money1 = Money(9, 50)
money2 = Money(5, 75)

money1.display()
money2.display()

money3 = money1.add(money2)
money3.display()

money4 = money1.subtract(money2)
money4.display()

# Изменение значений частей денег
money1.set_dollars(62)
money1.set_cents(30)
money1.display()
