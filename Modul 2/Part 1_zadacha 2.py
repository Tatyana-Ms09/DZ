num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

operation = input("Выберите операцию (максимум (1), минимум (2) или среднеарифметическое (3)): ")

if operation == "1":
    result = max(num1, num2, num3)
    print("Максимум из трех чисел:", result)
elif operation == "2":
    result = min(num1, num2, num3)
    print("Минимум из трех чисел:", result)
elif operation == "3":
    result = (num1 + num2 + num3) / 3
    print("Среднеарифметическое трех чисел:", result)
else:
    print("Неверный выбор операции. Пожалуйста, выберите '1', '2' или '3'.")
