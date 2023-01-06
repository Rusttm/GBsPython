# 5 Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = 13
def Fibb(n):
    result_fibb = [0,1]
    for i in range(2,n+1):
        result_fibb.append(result_fibb[i-1] + result_fibb[i-2])
    return result_fibb

def NegFibb(fib_list):
    lenth = len(fib_list)
    result_nfibb = []
    for i in range(lenth-1):
        result_nfibb.append(fib_list[lenth-i-1]*(-1)**(lenth-i))
    return result_nfibb+fib_list

print(f'Для {n}: {NegFibb(Fibb(n))}')