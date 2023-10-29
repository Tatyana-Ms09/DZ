meters = float(input("Введите количество метров: "))

units = input("Выберите единицы измерения (мили (м), дюймы (д) или ярды (я)): ")

miles_conversion = 0.000621371
inches_conversion = 39.3701
yards_conversion = 1.09361

if units == "м":
    result = meters * miles_conversion
    print("Это равно", result, "миль")
elif units == "д":
    result = meters * inches_conversion
    print("Это равно", result, "дюймов")
elif units == "я":
    result = meters * yards_conversion
    print("Это равно", result, "ярдов")
else:
    print("Неверный выбор единиц измерения. Пожалуйста, выберите 'м', 'д' или 'я'.")
