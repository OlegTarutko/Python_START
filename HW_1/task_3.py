"""
Напишите программу, которая принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Ввод: два значения типа <int>
Вывод: значение типа <int> либо значение типа <str>

Пример:

34
-30
4

2
4
1

-34
0
Точка на отрицательной части оси абсцисс
"""
x = float(input('Enter X coordinate: '))
y = float(input('Enter Y coordinate: '))
if x > 0 and y > 0:
    print('first quarter')
elif x < 0 and y > 0:
    print('second quarter')
elif x < 0 and y < 0:
    print('third quarter')
elif x > 0 and y < 0:
    print('fourth quarter')
elif x == 0 and y < 0:
    print('Point on the negative part of the y-axis')
elif x == 0 and y > 0:
    print('Point on the positive part of the y-axis')
elif x > 0 and y == 0:
    print('Point on the positive part of the x-axis')
elif x < 0 and y == 0:
    print('Point on the negative part of the x-axis')
