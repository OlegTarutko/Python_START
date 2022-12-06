"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""
from random import randint
from os import path, mkdir, chdir

k = int(input('Enter polynomial degree: '))
lst = [randint(0, 100) for number in range(k)]


def new_polynomial(lst):
    if sum(lst) == 0:
        return '0=0'
    i = len(lst) - 1
    result = []
    for num in lst:
        if num:
            if i == 0:
                result.append(f'{num}')
            elif num == 1:
                result.append(f'{num if num != 1 else ""}x')
            else:
                result.append(f'{num if num != 1 else ""}x^{i}')
        i -= 1
    return ' + '.join(result) + ' =0'


polynomial = new_polynomial(lst)
print(polynomial)
