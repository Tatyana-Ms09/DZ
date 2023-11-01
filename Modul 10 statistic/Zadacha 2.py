class TemperatureConverter:
    conversion_count = 0  
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversion_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.conversion_count

celsius_temperature = 30
fahrenheit_temperature = TemperatureConverter.celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} градусов Цельсия = {fahrenheit_temperature} градусов Фаренгейта")

celsius_temperature = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} градусов Фаренгейта = {celsius_temperature} градусов Цельсия")

print("Количество конвертаций:", TemperatureConverter.get_conversion_count())
