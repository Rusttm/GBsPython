# Функции


def MultiParams(*params):
    for p in params:
        print(p)

# MultiParams(1,2,3,4,5)

# Кортежи

my_tuple = (3, 4,)
print(my_tuple[0])
# my_tuple[0] = 5 - Ошибка!: неизменяемый тип
for item in my_tuple:
    print(item)


# словари

dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←


# типы ключей могут отличаться

print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))

for key,value in dictionary.items(): # for (k,v) in dictionary.items():
    print(f'{key}: {value}')

# Множества
a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(b) # set
a.remove(3)
a.discard(7) # не вызывает ошибок
print(a)

# операции с множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))

a = {1, 2, 3, 5, 8}
b = frozenset(a) # неизменяемые множества

# Списки
my_list = ['a','b','c','d']
my_list.pop(2)
my_list.insert(2, 'wz')
my_list.append('end')
print(my_list)