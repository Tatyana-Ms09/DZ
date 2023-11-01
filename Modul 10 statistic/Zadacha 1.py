class Fraction:
    count = 0  

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1  

    def input_data(self):
        self.numerator = int(input("Введите числитель: "))
        self.denominator = int(input("Введите знаменатель: "))

    def display_data(self):
        print(f"Дробь: {self.numerator}/{self.denominator}")

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def add(self, other_fraction):
        result_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        result_denominator = self.denominator * other_fraction.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self, other_fraction):
        result_numerator = (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
        result_denominator = self.denominator * other_fraction.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self, other_fraction):
        result_numerator = self.numerator * other_fraction.numerator
        result_denominator = self.denominator * other_fraction.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other_fraction):
        result_numerator = self.numerator * other_fraction.denominator
        result_denominator = self.denominator * other_fraction.numerator
        return Fraction(result_numerator, result_denominator)

    def simplify(self):
        common_factor = self.gcd(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def get_object_count():
        return Fraction.count

fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 8)

fraction1.display_data()
fraction2.display_data()

result = fraction1.add(fraction2)
result.display_data()

print("Количество созданных объектов класса 'Дробь':", Fraction.get_object_count())
