#  Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Enter the Number '))
my_dict = {x: round((1+1/x)**x,2) for x in range(1,n+1)}
print(f'Для N = {n} {my_dict}')
print(f'Сумма {sum(my_dict.values())}')