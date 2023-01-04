# для натурального n создать словарь индекс значение n:3n+1


n = int(input('Enter the Number '))


my_dict = dict()
for i in range(n):
    my_dict[i+1] = (i+1)*3 +1
print(f'Для n = {n}: {my_dict}')
