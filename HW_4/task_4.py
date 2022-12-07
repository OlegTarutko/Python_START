"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""
from sympy.abc import x
from sympy import *
from os import path, chdir, listdir

if path.isdir("polynomial"):  # Проверка наличия папки
    chdir("polynomial")
else:
    print("Каталог с файлами отсутствует")
    exit()

lst_polynomial = []  # Создание пустого списка.
for file_name in listdir():
    if "polynomial_" in file_name:  # Проверка наличия файлов.
        with open(file_name, 'r') as file:
            str_polynomial = file.read()
            print(f"{str_polynomial} from file {file_name}")
            lst_polynomial.append(str_polynomial)
print(lst_polynomial)


def sum_polynomial(*args):
    res = []
    for arg in args:
        s = arg.replace('x', ' * x').replace('x^', 'x ** ').replace(' = 0', '')  # Перевод на Пайтон язык
        res.append(collect(s, x))
    return str(sum(res)).replace('*x', 'x').replace('**', '^') + ' = 0'  # Перевод обратно в математическую запись.


print(sum_polynomial(*lst_polynomial))

with open("sum_polynomial.txt", 'w') as file:  # Запись результата в файл.
    file.write(sum_polynomial(*lst_polynomial))
    print("Result is written to a file sum_polynom.txt")
