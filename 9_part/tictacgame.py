""" модуль игра в Крестики-нолики по телеграмму"""


class XOgame():
    def __init__(self, user_name='1') -> None:
        import random
        self.user_name = user_name
        self.rand = random
        self.my_field = [[0 for _ in range(3)] for _ in range(3)]
        self.my_field_string = str('| a  b  c \n'+'| _  _  _ |1\n'+'| _  _  _ |2\n'+'| _  _  _ |3\n'+'  --------- ')
        self.coord_list = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        self.current_player = 0
        self.human_player = 0
        self.bot_player = 0
        self.game_type = 0 #0 - F2F and 1-Human vs Bot
        self.player_dict = {1:'X', -1:'O'}
        
    def PrintField(self):
        # return self.my_field_string
        # names_field = [['  _1__2__3_ '], ['a|', 'b|', 'c|']]
        # print(names_field[0][0])
        header_string = ' a   b   c \n'
        result_string = header_string
        for i, elem in enumerate(self.my_field):
            for ii, x in enumerate(elem):
                result_string += ''
                if x==0:
                    result_string += '\U00002796'
                elif x==-1:
                    result_string += '\U00002B55'

                elif x==1:
                    result_string += '\U0000274C'

                else:
                    result_string += f' {x} '
                
                if ii == 2:
                    result_string += f'{i+1}\n'
        return result_string


    def ChangeValue(self, coord='a1', value=1) -> bool:
        coord_dict = {'a': 0, 'b': 1, 'c': 2, '1': 0, '2': 1, '3': 2}
        x, y = coord
        
        if self.my_field[coord_dict[y]][coord_dict[x]] == 0:
            self.my_field[coord_dict[y]][coord_dict[x]] = value
            return True
        return False

    def CheckWin(self) -> list:
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
        if ( winer == 3 * self.human_player ):
            # print('You WIN!!!')
            return ["end", 'You WIN!!!\U0001F973']
        elif ( winer == 3 * self.bot_player):
            # print('Your opponent win!')
            return ["end", 'I win!\U0001F973']

        # проверяем окончание игры
        is_filled = 0
        for i in range(3):
            for ii in range(3):
                if self.my_field[i][ii] != 0:
                    is_filled += 1
        if is_filled == 9:
            # print('End Game!')
            return ["end", 'Nobody win\U0001F91D End Game!']

        return ["continue", "Next turn"]
    

    def UserTurn(self, coordinate='b2'):

        coordinate = coordinate.lower()

        if coordinate == 'x':
            self.human_player = 1
            self.bot_player = -1
            return ["continue", "Отлично, Вы играете \U0000274C, Ваш ход"] # крестики
        elif coordinate == 'o':
            self.human_player = -1
            self.bot_player = 1
            return ["continue", "Отлично, Вы играете \U00002B55, Ваш ход"] # нолики
        elif not self.human_player:
            return ["continue", "Чем Вы будете играть? 'O' или 'X'"]


        if (coordinate not in self.coord_list) and (coordinate not in ['o', 'x']):
            return ["continue", f"Координата должна иметь вид {self.coord_list}"]
        else:
            if self.ChangeValue(coord=coordinate, value=self.human_player):
                win = self.CheckWin()

                if win[0] == "continue":
                    self.BotTurn()
                    return ["continue", f"{self.PrintField()}"]
                else:
                    # return self.CheckWin()
                    return ["end", f"{self.PrintField()}\n{win[1]}"]
            else:
                return ["continue", f"Поле занято\n{self.PrintField()}"]


    def BotTurn(self):
        while True:
            for i in range(3):
                for ii in range(3):
                    if self.my_field[i][ii] == 0:
                        if self.rand.randint(0, 9) == 1:
                            self.my_field[i][ii] = self.bot_player
                            # print('Бот походил:')
                            # self.PrintField()
                            return True
                        else:
                            continue
        



        


if '__name__' == '__main__':
    new_game = XOgame()
    print(new_game.PrintField())

