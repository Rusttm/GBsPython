# 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


n = int(input('Enter N: '))

def DelNumber(n):
    result = []
    for i in range(1,n+1):
        if (n%i == 0):
            result.append(i)
    return result

def SimpleDelNumber(del_list):
    result_list = []
    for _ in range(len(del_list)):
        elem = del_list.pop()
        if len(DelNumber(elem)) <= 2:
            result_list.append(elem)
    return result_list

print(f'Список множителей числа {n}: {DelNumber(n)}')
print(f'Список простых множителей числа {n}: {SimpleDelNumber(DelNumber(n))}')