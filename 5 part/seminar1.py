# # 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open(r'seminar1_file.txt', 'w') as f:
    f.write('1 2 3 \n 4 5 7 8 9')

# считываем из файла 
with open('seminar1_file.txt', 'r') as f:
    # file_string = f.readline()
    file_strings = f.readlines()

num_row = []
for file_string in file_strings:
    num_row.append(list(map(int, file_string.split())))

print(num_row)