# список уникальных элементов заданной последовательности
# [1,2,3,4,5,4,2,10] => [1,3,5,10]

s = input('Введите последовательность')

def Str2List(s: str) -> list:
    
    return [int(elem) for elem in s[1:-1].split(',')]

def Unic(my_list: list) -> list:
    result_list = []
    for elem in my_list:
        if my_list.count(elem) == 1:
            result_list.append(elem)
    return result_list

print(Unic(Str2List(s)))
