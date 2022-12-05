"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.

Ввод: значение типа <int>
Вывод: значение типа <int>

Примеры:
45
101101

3
11

2
10
"""
number = int(input("Please enter number: "))
lst = ''

while number > 0:
    lst = str(number % 2) + lst
    number //= 2
print(int(lst))
