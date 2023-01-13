# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

file_4code = '5dz3_rle_4code.txt'
file_coded = '5dz3_rle_coded.txt'
file_decoded = '5dz3_rle_decoded.txt'

my_textes = []

# читаем из файла
with open(file_4code, 'r') as f1:
    my_textes = f1.readlines()

print(f'Прочитано из файла для кодирования {my_textes}')

# кодер одной строки
def LineCoder(my_string: str) -> str:
    result_line = ''
    current_char = my_string[0]
    counter = 0
    for i in range(len(my_string)):
        if current_char == my_string[i]:
            counter += 1
        else:
            result_line += f'{counter}{my_string[i-1]}'
            counter = 1
        current_char = my_string[i]
    return result_line


# кодируем по строкам и пишем в файл
with open(file_coded, 'w') as f2:
    for elem in my_textes:
        f2.write(f'{LineCoder(elem)}\n')


# считываем закодированный файл по строкам
coded_textes = []
with open(file_coded, 'r') as f3:
    coded_textes = f3.readlines()

print(f'Прочитано из файла для декодирования {coded_textes}')


