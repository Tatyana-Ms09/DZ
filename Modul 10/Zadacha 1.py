class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __lt__(self, other_circle):
        return self.radius < other_circle.radius

    def __gt__(self, other_circle):
        return self.radius > other_circle.radius

    def __le__(self, other_circle):
        return self.radius <= other_circle.radius

    def __ge__(self, other_circle):
        return self.radius >= other_circle.radius

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        else:
            raise ValueError("Unsupported operand type for +")

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        else:
            raise ValueError("Unsupported operand type for -")

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        else:
            raise ValueError("Unsupported operand type for +=")

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            return self
        else:
            raise ValueError("Unsupported operand type for -=")

    def __str__(self):
        return f"Circle with radius {self.radius}"

circle1 = Circle(4)
circle2 = Circle(6)

print(circle1 == circle2)  
print(circle1 < circle2)   
print(circle1 > circle2)   
print(circle1 <= circle2)  
print(circle1 >= circle2) 

circle1 += 2
print(circle1)  

circle2 -= 3
print(circle2)  
