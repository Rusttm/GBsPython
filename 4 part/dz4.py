# 4 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Введите степень уравнения:'))
# from sympy import *
import random

# составляем список случайных коэффициентов
coef_list = []
for i in range(k+1):
    coef = random.randint(0,101)
    coef_list.append(coef)

# составляем список степеней
x_list = [str(f'x**{i}') if i!=1 else str(f'x') for i in range(k,0,-1)]

# создаем строку уравнения
result_string = ''
for i in range(k):
    if (coef_list[i] != 0):
        result_string += f'{coef_list[i]}*{x_list[i]}'
        if coef_list[i+1] > 0:
            result_string += ' + '
result_string += f'{coef_list[k]} = 0'

# записываем в файл
with open('dz4_file.txt', 'w') as f:
    f.write(result_string)

print(result_string)

# x = Symbol('x')
# expr = x**2 + x + 5
# print(expr)
