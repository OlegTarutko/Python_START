"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""
# path = 'indexes.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
N = int(input('Enter N: '))
import random

rnd_list = []
for i in range(N):     # range от 0 до N
    rnd_list.append(random.randint(-N, N))
print(rnd_list)

with open("indexes.txt") as data: index_list = [int(line.strip()) for line in data]
# 5

mult = 1
# for i in range(len(rnd_list)):
#     if i in index_list:
#         mult *= rnd_list[i]
#     if -i in index_list and i != 0:
#         mult *= rnd_list[-i]
for i in range(-N, N):
    if i in index_list:
        mult *= rnd_list[i]
print(mult)
