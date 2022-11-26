"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""
num = float(input('Enter number: '))
str_number = str(num)
sum = 0
for i in range(len(str_number)):
    if str_number[i].isdigit():
        sum += int(str_number[i])
print(sum)
