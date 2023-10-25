expression = input("Введите арифметическое выражение (например, 23+12): ")

try:
    # Попробуйте вычислить результат выражения
    result = eval(expression)
    print("Результат:", result)
except Exception as e:
    print("Ошибка:", e)