# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

n = int(input('Enter the day number - '))

def WeekDay(n):
    if n in list(range(1,6)):
        print(f'{n} -> нет')
    else:
        print(f'{n}-> да')

WeekDay(n)