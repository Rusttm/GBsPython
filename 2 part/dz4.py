# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.



n = int(input('Enter the Number '))

if (n<0): n = -n
my_array = list(range(-n,n+1))
print(my_array)