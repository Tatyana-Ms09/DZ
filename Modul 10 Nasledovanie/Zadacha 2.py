class Ship:
    def __init__(self, name, displacement, length, max_speed):
        self.name = name
        self.displacement = displacement
        self.length = length
        self.max_speed = max_speed

    def info(self):
        print(f"Корабль: {self.name}")
        print(f"Водоизмещение: {self.displacement} тонн")
        print(f"Длина: {self.length} метров")
        print(f"Максимальная скорость: {self.max_speed} узлов")

class Frigate(Ship):
    def __init__(self, name, displacement, length, max_speed, missile_system):
        super().__init__(name, displacement, length, max_speed)
        self.missile_system = missile_system

    def launch_missiles(self):
        print(f"Запуск ракет из системы {self.missile_system}")

class Destroyer(Ship):
    def __init__(self, name, displacement, length, max_speed, artillery_guns):
        super().__init__(name, displacement, length, max_speed)
        self.artillery_guns = artillery_guns

    def fire_guns(self):
        print(f"Открытие огня с артиллерийских пушек: {self.artillery_guns}")

class Cruiser(Ship):
    def __init__(self, name, displacement, length, max_speed, radar_system):
        super().__init__(name, displacement, length, max_speed)
        self.radar_system = radar_system

    def scan_area(self):
        print(f"Сканирование радарной системой: {self.radar_system}")

frigate = Frigate("UA 333", 9500, 105, 40, "Leopard")
frigate.info()
frigate.launch_missiles()

destroyer = Destroyer("UA 777", 13500, 150, 50, "F16")
destroyer.info()
destroyer.fire_guns()

cruiser = Cruiser("UA 009", 23500, 152, 22, "Granit")
cruiser.info()
cruiser.scan_area()
