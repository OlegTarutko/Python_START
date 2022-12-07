"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""
number = int(input('Enter number: '))
lst = []
counter = 2
while number > 1:
    if (number % counter) != 0:
        counter += 1
    else:
        lst.append(counter)
        number /= counter
print(lst)
