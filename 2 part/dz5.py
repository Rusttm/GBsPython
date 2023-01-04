# Реализуйте алгоритм перемешивания списка.


import random

n = int(input('Задайте количество элементов в списке: '))
my_array = list(range(1,n+1))
print(f' Для массива {my_array}', end=' -> ')
random_list = []
for i in range(n):
    elem = my_array.pop(random.randint(0,n-i-1))
    random_list.append(elem)
print(random_list)