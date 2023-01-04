# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1,y1 = [int(coord) for coord in input('Enter A ')[1:-1].split(',')]
x2,y2 = [int(coord) for coord in input('Enter B ')[1:-1].split(',')]
def Distance(x1,y1,x2,y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print(f'A({x1},{y1}); B({x2},{y2}) -> {round(dist,2)}')

Distance(x1,y1,x2,y2)