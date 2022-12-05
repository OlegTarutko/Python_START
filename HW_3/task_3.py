"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
import random

number = int(input("Enter number: "))
lst = [round(random.uniform(1, 9), 2) for i in range(number)]
lst_2 = []

for i in range(number):
    lst_2.append(lst[i] % 1)
result = max(lst_2) - min(lst_2)

print(lst)  # Для проверки работоспособности.
print(round(result, 2))
