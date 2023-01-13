# Создайте программу для игры в ""Крестики-нолики"".


class XOgame():
    def __init__(self) -> None:
        self.my_field = [[0 for _ in range(3)] for _ in range(3)]
        self.coord_list = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        self.current_player = 0
        self.player_dict = {1:'X', -1:'O'}
        
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
        winer = 0
        # проверяем строки
        for i in range(3):
            if (sum(self.my_field[i])==-3):
                winer = -3 
            elif (sum(self.my_field[i])==3):
                winer = 3
        
        # проверка вертикалей
        verticals = [0 for _ in range(3)]
        for i in range(3):
            for ii in range(3):
                verticals[ii] += self.my_field[i][ii]
        if (-3 in verticals):
            winer = -3 
        elif (3 in verticals):
            winer = 3

        # проверка перекрестков
        crosses = [0,0]
        crosses[0] = self.my_field[0][0] + self.my_field[1][1] + self.my_field[2][2]
        crosses[1] = self.my_field[0][2] + self.my_field[1][1] + self.my_field[2][0]
        if (-3 in crosses):
            winer = -3 
        elif (3 in crosses):
            winer = 3

        # ищем победителя
        if ( winer == -3 ):
            print('O is winer!') 
            return True
        elif ( winer == 3 ):
            print('X is winer!')
            return True

        # проверяем окончание игры
        is_filled = 0
        for i in range(3):
            for ii in range(3):
                if self.my_field[i][ii] != 0:
                    is_filled += 1
        if is_filled == 9:
            print('End Game!')
            return True

        return False

    def PlayerTurn(self):
        coord = 'xx'
        while coord not in self.coord_list:
            coord = input(f'Please enter coordinate for {self.player_dict[self.current_player]} or q for quit: ')
            if coord == 'q':
                print('Quit!')
                return False
        
        self.ChangeValue(coord=coord, value=self.current_player)
        self.PrintField()
        return True




    def GameStart(self):
        while self.current_player not in [-1,1]:
            self.current_player = int(input('Введите, чем будете играть? O:-1 X:1 '))
        while True:
            if not self.PlayerTurn():
                return
            if self.CheckWin():
                print('END Game')
                return
        
        


my_game = XOgame()

my_game.GameStart()
# print(my_game.ChangeValue(coord='a3', value=1))
# my_game.ChangeValue(coord='b2', value=1)
# my_game.ChangeValue(coord='c1', value=1)
# my_game.PrintField()
# my_game.CheckWin()