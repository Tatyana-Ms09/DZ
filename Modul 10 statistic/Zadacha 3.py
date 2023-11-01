class LengthConverter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        return miles / 0.621371

meters_length = 100
feet_length = LengthConverter.meters_to_feet(meters_length)
print(f"{meters_length} метров = {feet_length} футов")

feet_length = 328.084
meters_length = LengthConverter.feet_to_meters(feet_length)
print(f"{feet_length} футов = {meters_length} метров")

kilometers_length = 100
miles_length = LengthConverter.kilometers_to_miles(kilometers_length)
print(f"{kilometers_length} километров = {miles_length} миль")

miles_length = 6.21371
kilometers_length = LengthConverter.miles_to_kilometers(miles_length)
print(f"{miles_length} миль = {kilometers_length} километров")
