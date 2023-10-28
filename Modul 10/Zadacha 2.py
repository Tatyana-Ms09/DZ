class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag
            return Complex(real_part, imag_part)
        else:
            raise ValueError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Complex):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag
            return Complex(real_part, imag_part)
        else:
            raise ValueError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        else:
            raise ValueError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Complex):
            divisor = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag) / divisor
            imag_part = (self.imag * other.real - self.real * other.imag) / divisor
            return Complex(real_part, imag_part)
        else:
            raise ValueError("Unsupported operand type for /")

    def __str__(self):
        return f"{self.real} + {self.imag}i"

complex1 = Complex(4, 2)
complex2 = Complex(1, 7)

result_add = complex1 + complex2
result_sub = complex1 - complex2
result_mul = complex1 * complex2
result_div = complex1 / complex2

print(result_add)  
print(result_sub)  
print(result_mul)  
print(result_div)  
