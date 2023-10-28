class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model

    def __add__(self, passengers):
        if isinstance(passengers, int):
            if self.current_passengers + passengers <= self.max_passengers:
                self.current_passengers += passengers
            else:
                raise ValueError("Too many passengers to add")
        else:
            raise ValueError("Unsupported operand type for +")
        return self

    def __sub__(self, passengers):
        if isinstance(passengers, int):
            if self.current_passengers - passengers >= 0:
                self.current_passengers -= passengers
            else:
                raise ValueError("Not enough passengers to remove")
        else:
            raise ValueError("Unsupported operand type for -")
        return self

    def __iadd__(self, passengers):
        return self.__add__(passengers)

    def __isub__(self, passengers):
        return self.__sub__(passengers)

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers

    def __str__(self):
        return f"Model: {self.model}, Max Passengers: {self.max_passengers}, Current Passengers: {self.current_passengers}"

plane1 = Airplane("A 222", 166)
plane2 = Airplane("B 333", 233)

print(plane1 == plane2)  

plane1 += 100
print(plane1)  

plane2 -= 200
print(plane2)  

print(plane1 < plane2) 
print(plane1 >= plane2) 

