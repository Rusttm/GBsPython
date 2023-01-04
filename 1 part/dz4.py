# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


q = int(input('Enter Quadrant = '))

def QuadrantRange(q):
    if (q==1): print('X>0, Y>0')
    if (q==2): print('X<0, Y>0')
    if (q==3): print('X<0, Y<0')
    if (q==4): print('X>0, Y<0')

QuadrantRange(q)