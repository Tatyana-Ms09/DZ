class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price

    def __str__(self):
        return f"Area: {self.area} sq. ft, Price: ${self.price}"

flat1 = Flat(300, 500000)
flat2 = Flat(200, 240000)
flat3 = Flat(100, 200000)

print(flat1 == flat2)  
print(flat2 != flat3)  
print(flat1 < flat2)  
print(flat2 >= flat3)  
