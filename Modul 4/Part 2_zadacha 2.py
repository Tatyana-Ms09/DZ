import random

random_list = [random.randint(-10, 10) for _ in range(20)]

min_element = float('inf')
max_element = float('-inf')
negative_count = 0
positive_count = 0
zero_count = 0

for num in random_list:
    if num < min_element:
        min_element = num  
    if num > max_element:
        max_element = num  
    if num < 0:
        negative_count += 1  
    elif num > 0:
        positive_count += 1 
    else:
        zero_count += 1 

print("Список целых чисел:", random_list)
print("Минимальный элемент:", min_element)
print("Максимальный элемент:", max_element)
print("Количество отрицательных элементов:", negative_count)
print("Количество положительных элементов:", positive_count)
print("Количество нулей:", zero_count)