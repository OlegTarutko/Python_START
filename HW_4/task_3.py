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

# Здравствуйте! Мне сложно далось данное домашнее задание, если честно. Код взят из семинара,
# понимаю что плохо, но по крайней мере я его полностью изучил, переделал частично, и сделал ренейм переменных,
# для своего удобства.
# Если честно, то не понял зачем в коде использовалось 'if __name__ == '__main__':', точнее я понимаю что этот код
# делает, но вот зачем он использовался в этих случаях не понял.

from random import randint
from os import path, mkdir, chdir

k = int(input('Enter polynomial degree: '))  # Коэффициент полинома
lst = [randint(0, 100) for number in range(k)]


def new_polynomial(lst):  # создание полинома степени К
    if sum(lst) == 0:  # Проверка на 0
        return '0 = 0'
    i = len(lst) - 1
    result = []
    for num in lst:
        if num:
            if i == 0:
                result.append(f'{num}')  # значение без переменной
            elif i == 1:
                result.append(f'{num if num != 1 else ""}x')  # Без 1
            else:
                result.append(f'{num if num != 1 else ""}x^{i}')  # степени
        i -= 1
    return ' + '.join(result) + ' = 0'


polynomial = new_polynomial(lst)  # Вызов функции создания полинома
print(polynomial)

if not path.isdir("polynomial"):  # Проверка наличия файла с текущим именем и создание нового.
    mkdir("polynomial")  # Создание папки
chdir("polynomial")  # проверка файла
i = 0
while True:
    if not path.isfile(f"polynomial_{i}.txt"):
        with open(f"polynomial_{i}.txt", 'w') as file:
            file.write(polynomial)
            print(f"polynomial written to file polynomial_{i}.txt")
        break
    else:
        i += 1
