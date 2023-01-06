# найдите корнии квадратного уравнения
# 1. с помощью формул
# 2. с помощью дополнительных модулей

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

def Equation1(a,b,c):
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print('Решений нет')
    elif discriminant == 0:
        x = - b/2*a
        print(f'Решение уравнения одно {x=}')
    else:
        x1 = (-b + discriminant**0.5)/2*a
        x2 = (-b - discriminant**0.5)/2*a
        print(f'Решения уравнения: {x1=} {x2=}')

def Equation2(a,b,c):

    

Equation1(a,b,c)


