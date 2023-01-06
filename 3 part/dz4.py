# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = 2

def Dec2Bin(number, s=''):
    if (number in [0,1]): return (number, f'{number}{s}')
    return (Dec2Bin(number//2, f'{number%2}{s}'))

print(f'{number} -> {Dec2Bin(number)[1]}')