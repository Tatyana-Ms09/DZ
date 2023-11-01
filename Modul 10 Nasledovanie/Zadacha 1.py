class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def info(self):
        print(f"Устройство: {self.brand} {self.model}")
        print(f"Мощность: {self.power} Вт")

class CoffeeMachine(Device):
    def __init__(self, brand, model, power, coffee_type):
        super().__init__(brand, model, power)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"Приготовление кофе типа {self.coffee_type}")

class Blender(Device):
    def __init__(self, brand, model, power, functions):
        super().__init__(brand, model, power)
        self.functions = functions

    def blend(self):
        print("Приготовление напитка или блюда с использованием блендера")

class MeatGrinder(Device):
    def __init__(self, brand, model, power, blade_type):
        super().__init__(brand, model, power)
        self.blade_type = blade_type

    def grind_meat(self):
        print(f"Измельчение мяса с использованием мясорубки с лезвиями типа {self.blade_type}")

coffee_machine = CoffeeMachine("Philips", "H3033", 1300, "Арабика")
coffee_machine.info()
coffee_machine.make_coffee()

blender = Blender("Braun", "Multiquick 5", 800, ["Измельчение"])
blender.info()
blender.blend()

meat_grinder = MeatGrinder("Kenwood", "M050", 1500, "Сменные ножи")
meat_grinder.info()
meat_grinder.grind_meat()

