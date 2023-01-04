# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input('Enter the Number '))
num_array = [1]
mult_array = ['1']
for i in range(1,n):
    num_array.append((i+1)*num_array[i-1])
    mult_array.append(f'{mult_array[i-1]}*{(i+1)}')

print(f'пусть N = {n}, тогда {num_array} (tuple(mult_array))')

