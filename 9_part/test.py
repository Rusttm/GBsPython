import candygame

# games = [candygame.CandyGame(user_name=f'{i}') for i in range(4)]
# games = dict()
# games[1] = candygame.CandyGame(user_name='1')
# print(games[1].UserTurn(5))
# print(games[1].UserTurn(3))
# print(games[1].UserTurn(3))
#
#
# print('lkaHIUHB'.lower())
# print('\N{Sauropod}')
# print('\N{Candy}')
# print('\U0001F534')
# print('::bangbang::')
# print('\U00002B55')
# print('\U00002B55')
# print('\U0000274C')
# print('\U0000274C')

field_data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
accord = {0: "\U00002796", 1: "\U0000274C", -1: "\U00002B55"}

print(list(map(lambda x: list(map(lambda y: accord[y], x)), field_data)))