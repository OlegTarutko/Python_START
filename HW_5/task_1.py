"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""
str_text = "забвение аптека компьютер семинар автомобиль"
letters = "абв"
str_val = []

value = str_text.split()
for word in value:
    if not (letters[0] in word and letters[1] in word and letters[2] in word):
        str_val.append(word)
print(" ".join(str_val))
