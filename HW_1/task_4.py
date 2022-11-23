"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
в этой четверти (x и y).

Ввод: значение типа <int>
Вывод: значение типа <str>

Пример:

3
x < 0, y < 0
"""
q = int(input("Enter quarter number: "))
if q == 1:
    print("x > 0 and y > 0")
elif q == 2:
    print("x < 0 and y > 0")
elif q == 3:
    print("x < 0 and y < 0")
elif q == 4:
    print("x > 0 and y < 0")
else:
    print("Please enter a value from 1 to 4")