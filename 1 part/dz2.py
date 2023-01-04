# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

checker = [[0,0,0], 
            [0,0,1],
            [0,1,0],
            [0,1,1],
            [1,0,0],
            [1,0,1],
            [1,1,0],
            [1,1,1]]
for [x,y,z] in checker:
    check = (not (x or y or z)) == ( (not x) and (not y) and (not z))
    print(x,y,z, check, end=' : ')
    print(f'not ({x} or {y} or {z}) = {not (x or y or z)}' , end=' <-> ')
    print(f'(not {x} and not {y} and not {z}) = {(not x) and (not y) and (not z)}')
