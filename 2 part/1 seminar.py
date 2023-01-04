# принимает число N, выдает N случайных чисел

import random

n = int(input('Enter the Number '))

def RandomPrint(n):
    print(f'Для N = {n}: ', end='')
    for _ in range(n-1):
        print(random.randint(-99, 100), end=',')
    print(random.randint(-99, 100))

RandomPrint(n)