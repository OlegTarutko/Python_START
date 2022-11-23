"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""
#  not (x or y or z) = not x and not y and not z        //Это для себя. Перевод символов.

x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

print(not (x or y or z) == (not x and not y and not z))
