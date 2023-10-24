def print_rectangle(height, width):
    for i in range(height):
        print("*" * width)

def print_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

while True:
    print("Меню:")
    print("1. Вывести треугольник из звездочек")
    print("2. Выйти")

    choice = input("Выберите опцию (1/2): ")

    if choice == '1':
        height = int(input("Введите высоту треугольника: "))
        print_triangle(height)
    elif choice == '2':
        print("Выход")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")