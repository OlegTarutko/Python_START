"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""
#  not (x or y or z) = not x and not y and not z        //Это для себя. Перевод символов.

x, y, z = 0, 0, 0
print(not (x or y or z) == (not x and not y and not z))
