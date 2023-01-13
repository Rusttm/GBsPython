# Создайте программу для игры в ""Крестики-нолики"".



my_field = [[0 for _ in range(3)] for _ in range(3)]

def PrintField(my_field: list):
    names_field = [['  _1__2__3_ '], ['a|', 'b|', 'c|']]
    print(names_field[0][0])
    for i, elem in enumerate(my_field):
        print(names_field[1][i], end='')
        for ii, x in enumerate(elem):
            if x==0:
                print(' _ ', end='')
            elif x==-1:
                print(' O ', end='')
            elif x==1:
                print(' X ', end='')
            else:
                print(f' {x} ', end='')
            
            if ii == 2:
                print('|')
    print('  _________ ')

def ChangeValue(my_field: list, coord='a1', value=1) -> list:
    coord_dict = {'a':0, 'b':1, 'c':2, '1':0, '2':1, '3':2}
    y,x = coord
    my_field[coord_dict[y]][coord_dict[x]] = value
    return my_field

def CheckWin(my_field: list) -> str:
    
        

ChangeValue(my_field, coord='c3', value=1)
ChangeValue(my_field, coord='a1', value=1)
ChangeValue(my_field, coord='b2', value=1)
PrintField(my_field)