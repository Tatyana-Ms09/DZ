def Произведение(список):
    proizved = 1
    for число in список:
        proizved *= число
    return proizved

список = [2, 3, 4, 1]
результат = Произведение(список)
print(f"Произведение элементов списка: {результат}")