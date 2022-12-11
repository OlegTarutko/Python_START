"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""
from random import randint
from time import sleep

while True:
    try:
        game_mode = int(input('Выберете с кем хотите сыграть:\n1 - человек\n2 - непобедимый bOT\nВведите цифру:\n'))
    except ValueError:
        print('Введите цифру 1 или 2!')
    else:
        break


candies = int(input("Введите количество конфет на столе: "))
k = int(input("Сколько конфет будем брать за один раз? "))

print(f'На столе {candies} конфет. За один ход можно забрать не более чем {k} конфет')


# Функция игры человека
def game_candies(name, candy):
    while True:
        try:
            player_candies = int(input(f'{name}, сколько конфет вы хотите взять?\n'))
        except ValueError:
            print('Введите число!')
        else:
            break
    if player_candies > k:
        print(f'За один ход можно забрать не более чем {k} конфет')
    elif player_candies < 1:
        print('Надо обязательно взять хотя бы одну конфету')
    elif player_candies <= k:
        candy -= player_candies
        if candy < 0:
            candy = 0
            player_candies = "последние конфеты"
        print(f'{name}, взял {player_candies} шт. Осталось {candy}')
        return player_candies


# Функция бота
def is_bot(candys):
    lose_numbers = [i * k for i in range(1, candys + 1)]
    for i in range(candys - k, candys + 1):
        if candys in lose_numbers:
            return randint(1, k)
        elif i % k == 0:
            return candys - i


# Фразы бота
def bot_talk():
    num = randint(1, 3)
    sleep(1)
    if num == 1:
        print('bOT: хм...')
    elif num == 2:
        print('bOT: Проще простого)')
    elif num == 3:
        print('bOT: А ты хорош')
    else:
        return
    sleep(2)


# Игра с человеком
if game_mode == 1:
    first_player_name = input("Введите имя первого игрока\t")
    second_player_name = input("Введите имя второго игрока\t")
    lst_players = [first_player_name, second_player_name]
    first_move = randint(0, 1)
    i = first_move
    print(f'{lst_players[i]} ходит первый')
    while candies > 0:
        candy = game_candies(lst_players[i], candies)
        if candy:
            candies -= candy
            if candies < 1:
                print(f'{lst_players[i]} победил')
            i += 1
        if i >= len(lst_players):
            i = 0

# Игра с ботом
if game_mode == 2:
    first_player_name = input("Введите имя первого игрока\t")
    sleep(1)
    print('bOT: Первый ход твой, даю тебе шанс...')
    while candies > 0:
        candy = game_candies(first_player_name, candies)
        if candy:
            candies -= candy
            if candies < 1:
                print(f'{first_player_name} победил')
                break
            bot_candy = is_bot(candies)
            candies -= bot_candy
            bot_talk()
            print(f'bOT: Я возьму {bot_candy} шт. Осталось {candies}')
            if candies < 1:
                print(f'bOt победил!')

