"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)

Пример:
6
True

7
True

1
False
"""
a = int(input("Please enter number(1-7) day of the week: "))
print(a == 6 or a == 7)
