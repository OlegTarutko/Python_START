"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Результат округлить до сотых.

Ввод: четыре значения типа <int>
Вывод: значение типа <float>

Пример:

4 10
11 5
9.22
"""
x1 = int(input("Enter x1 coordinate: "))
y1 = int(input("Enter y1 coordinate: "))
x2 = int(input("Enter x2 coordinate: "))
y2 = int(input("Enter y2 coordinate: "))

S = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(round(S, 2))