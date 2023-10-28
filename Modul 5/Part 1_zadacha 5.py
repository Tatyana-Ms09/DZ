def Произведение (h1, h2):
    if h1 > h2:
        h1, h2 = h2, h1
    
    произведение = 1
    for число in range(h1, h2 + 1):
        произведение *= число
    return произведение

h1 = 5
h2 = 2

результат = Произведение (h1, h2)
print(f"Произведение чисел в диапазоне от {h1} до {h2} равно {результат}")
