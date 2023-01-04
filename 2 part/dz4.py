# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input('Enter the Number '))
pos1 = int(input('Enter the 1st position '))
pos2 = int(input('Enter the 2nd position '))

if (n<0): n = -n
my_array = list(range(-n,n+1))
random_list = []
for i in range(2*n+1):
    elem = my_array.pop(random.randint(0,2*n-i))
    random_list.append(elem)

print(f'Для N = {n}: {random_list}')
print(f'Произведение элементов {pos1} и {pos2} = {random_list[pos1]*random_list[pos2]}')