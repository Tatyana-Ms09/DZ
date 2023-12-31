размер_доски = 8
доска = [[-1 for _ in range(размер_доски)] for _ in range(размер_доски)]

def допустимый_ход(доска, x, y):
    return 0 <= x < размер_доски and 0 <= y < размер_доски and доска[x][y] == -1

def решить_задачу(доска, x, y, ход_номер):
    if ход_номер == размер_доски ** 2:
        return True

    ходы_x = [2, 1, -1, -2, -2, -1, 1, 2]
    ходы_y = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        новый_x = x + ходы_x[i]
        новый_y = y + ходы_y[i]
        if допустимый_ход(доска, новый_x, новый_y):
            доска[новый_x][новый_y] = ход_номер
            if решить_задачу(доска, новый_x, новый_y, ход_номер + 1):
                return True
            доска[новый_x][новый_y] = -1

    return False

начальная_x = int(input("Введите начальное положение коня по горизонтали (0-7): "))
начальная_y = int(input("Введите начальное положение коня по вертикали (0-7): "))

доска[начальная_x][начальная_y] = 0

if решить_задачу(доска, начальная_x, начальная_y, 1):
    print("Путь коня:")
    for строка in доска:
        print(строка)
else:
    print("Решение не найдено.")
    

    