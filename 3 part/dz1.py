# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
my_list = [2, 3, 5, 9, 3]

def SumOdd(my_list):
    result = 0
    for i in range(1,len(my_list),2):
        result += my_list[i]
    return result

print(f'{my_list} -> Ответ: {SumOdd(my_list)}')