def Delete (список, число):
    a = список.count(число)
    список = [элемент for элемент in список if элемент != число]
    return a

список1 = [2, 3, 4, 5, 3, 6, 3, 7, 8, 3]
Delete1 = 3

a = Delete(список1, Delete1)
print(f"Удалено {a} элементов из списка")
print("Исходный список:", список1)
