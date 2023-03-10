# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

def MultTwin(my_list):
    result_list = []
    half_len = int(len(my_list)/2+len(my_list)%2)
    for i in range(half_len):
        result_list.append(my_list[i]*my_list[len(my_list)-i-1])
    return result_list

print(f'{my_list} => {MultTwin(my_list)}')