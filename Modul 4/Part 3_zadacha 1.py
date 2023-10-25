import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

list3_union = list1 + list2

list3_unique = list(set(list1 + list2))

list3_intersection = list(set(list1) & set(list2))

unique_list1 = list(set(list1) - set(list2))
unique_list2 = list(set(list2) - set(list1))
list3_unique_elements = unique_list1 + unique_list2

list3_min_max = [min(list1), max(list1), min(list2), max(list2)]

print("Список 1:", list1)
print("Список 2:", list2)
print("Список, содержащий элементы обоих списков:", list3_union)
print("Список, содержащий элементы обоих списков без повторений:", list3_unique)
print("Список, содержащий элементы общие для двух списков:", list3_intersection)
print("Список, содержащий только уникальные элементы каждого из списков:", list3_unique_elements)
print("Список, содержащий только минимальное и максимальное значение каждого из списков:", list3_min_max)