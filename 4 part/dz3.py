# 3 Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


# 1 4 5 7 8 45 23 56 4 2

input_list = [int(x) for x in input('Введите последовательность: ').split()]
def ExplitDoubles(input_list):
    explit_list = []
    result_list = []
    for _ in range(len(input_list)):
        elem = input_list.pop(0)
        if (elem in input_list) or (elem in explit_list):
            explit_list.append(elem)
        else:
            result_list.append(elem)

    return result_list


print(f'Для последовательности {input_list}: {ExplitDoubles(input_list)}')