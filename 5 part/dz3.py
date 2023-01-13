# Создайте программу для игры в ""Крестики-нолики"".


class XOgame():
    def __init__(self) -> None:
        self.my_field = [[0 for _ in range(3)] for _ in range(3)]
        
    def PrintField(self):
        names_field = [['  _1__2__3_ '], ['a|', 'b|', 'c|']]
        print(names_field[0][0])
        for i, elem in enumerate(self.my_field):
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

    def ChangeValue(self, coord='a1', value=1) -> bool:
        coord_dict = {'a':0, 'b':1, 'c':2, '1':0, '2':1, '3':2}
        y,x = coord
        
        if self.my_field[coord_dict[y]][coord_dict[x]]==0:
            self.my_field[coord_dict[y]][coord_dict[x]] = value
            return True
        return False

    def CheckWin(self) -> str:
        '''проверка поля на выигрыш или окончание игры'''

        # проверяем строки
        for i in range(3):
            if (sum(self.my_field[i])==-3):
                print('O is winer!') 
            elif (sum(self.my_field[i])==3):
                print('X is winer!')
        
        # проверка вертикалей
        verticals = [0 for _ in range(3)]
        for i in range(3):
            for ii in range(3):
                verticals[ii] += self.my_field[i][ii]
        if (-3 in verticals):
            print('O is winer!') 
        elif (3 in verticals):
            print('X is winer!')

        # проверка перекрестков
        crosses = [0,0]
        crosses[0] = self.my_field[0][0] + self.my_field[1][1] + self.my_field[2][2]
        crosses[1] = self.my_field[0][2] + self.my_field[1][1] + self.my_field[2][0]
        if (-3 in crosses):
            print('O is winer!') 
        elif (3 in crosses):
            print('X is winer!')
        
        
        return True



            

    # self.ChangeValue(coord='a3', value=1)
    # self.ChangeValue(coord='b2', value=1)
    # self.ChangeValue(coord='c1', value=1)
    # self.PrintField()

my_game = XOgame()
my_game.PrintField()
print(my_game.ChangeValue(coord='a3', value=1))
my_game.ChangeValue(coord='b2', value=1)
my_game.ChangeValue(coord='c1', value=1)
my_game.PrintField()
my_game.CheckWin()