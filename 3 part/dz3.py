# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
my_list = [1.1, 1.2, 3.1, 5, 10.01]


def MinMaxRemind(my_list):
    max_elem = my_list[0]%1
    min_elem = my_list[0]%1
    for elem in my_list:
        if elem%1 >max_elem:
            max_elem = elem%1
        if elem%1 <min_elem and elem%1!=0:
            min_elem = elem%1
    return round(max_elem - min_elem,3)

print(f'{my_list} => {MinMaxRemind(my_list)}')