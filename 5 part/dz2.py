# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# 72*28=2016

import random

def CandyGameWin(num: int, ) -> int:
    '''возвращает лучшее решение или 28'''
    res =28
    if num%29:
        res = num%29
    return res


def CandiGameF2F(candies=2021):
    while candies>0:
        print(f'Осталось {candies}: ')
        get = int(input(f'1st Player (рекомендую {CandyGameWin(candies)}) -'))
        candies -= get
        if (candies == 0) : print('1st player WIN!') 
        print(f'Осталось {candies}: ')
        get = int(input(f'2nd Player (рекомендую {CandyGameWin(candies)}) -'))
        candies -= get
        if (candies == 0) : print('2nd player WIN!') 
    
def CandiGameBot(candies=2021):
    while candies>0:
        print(f'Осталось {candies}: ')
        if CandyGameWin(candies) == 28:
            get = int(input(f'Player (любое число) -'))
        else:
            get = int(input(f'Player (рекомендую {CandyGameWin(candies)}) -'))
        candies -= get
        if (candies == 0) : 
            print('Player WIN!')
            break
        print(f'Осталось {candies}: ')

        # AI бота - если игрок ошибается, то бот перехватывает инициативу
        if CandyGameWin(candies) == 28:
            get = random.randint(1,29)
        else:
            get = CandyGameWin(candies)
        print(f'Bot have got -{get}')
        candies -= get
        if (candies == 0) : 
            print('Bot WIN!')
            break


CandiGameBot(candies=100)
