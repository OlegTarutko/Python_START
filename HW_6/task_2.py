"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
import random

N = int(input('Enter N: '))

rnd_lst = []
for i in range(N):
    rnd_lst.append(random.randint(0, N))
print(rnd_lst)

lst_1 = []
lst_2 = []
lst_3 = list(set(rnd_lst))  # По вашей рекомендации с семинара.
for num in rnd_lst:
    if rnd_lst.count(num) == 1:
        lst_1.append(num)
    else:
        if lst_2.count(num) == 0:
            lst_2.append(num)

print(lst_1)
print(lst_2)
print(lst_3)
