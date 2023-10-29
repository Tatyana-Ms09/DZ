num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

operation = input("Выберите операцию (сумма(1) или произведение(2)): ")

if operation == "1":
    result = num1 + num2 + num3
    print("Сумма трех чисел:", result)
elif operation == "2":
    result = num1 * num2 * num3
    print("Произведение трех чисел:", result)
else:
    print("Неверный выбор операции. Пожалуйста, выберите '1' или '2'.")
