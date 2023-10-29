num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num1 == num2:
    print("Числа равны.")
else:
    if num1 < num2:
        print("Числа в порядке возрастания:", num1, num2)
    else:
        print("Числа в порядке возрастания:", num2, num1)
