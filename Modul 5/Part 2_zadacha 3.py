def Number (число):
    if число <= 1:
        return False
    for i in range(2, int(число ** 0.5) + 1):
        if число % i == 0:
            return False
    return True

def Number_Колич(список):
    простые = [число for число in список if Number(число)]
    return len(простые)

список = [3, 4, 5, 6, 7, 8, 9]
k = Number_Колич(список)
print(f"Количество простых чисел в списке: {k}")
