"""модуль для игры в конфетки с чатботом"""

class CandyGame:
    def __init__(self, candy_num=2023):
        self.candy_num = candy_num

    def CandyGameWin(self, num: int, ) -> int:
        '''возвращает лучшее решение или 28'''
        res =28
        if num%29:
            res = num%29
        return res

    def UserTurn(self, num:int) -> list:
        if num > 28 or num > self.candy_num:
            return ["continue", "возьмите, пожалуйста, меньше конфет (до 28)"]
        else:
            self.candy_num -= num
        bot_take = self.CandyGameWin(self.candy_num)
        self.candy_num -= num
        if self.candy_num == 0:
            return ["end", f"Я забрал {bot_take} конфет и выиграл!"]
        else:
            return ["continue", f"Я забрал {bot_take} конфет, осталось {self.candy_num}"]



if '__name__' == '__main__':
    new_game = CandyGame
