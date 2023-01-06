# задать строку чисел и вывести максимум и минимум


import random
from random import randrange

n = int(input('Введите количество чисел'))

list_num = [random.randint(-99,100) for _ in range(n)]

print(list_num, max(list_num), ' ', min(list_num))


if __name__ == '__main__':
    pass