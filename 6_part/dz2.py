# 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Enter number: '))

print(list(map(lambda x: [y for y in range(1,x+1)], filter(lambda m: n%m==0, range(1,n+1)) )))

# print(list(filter(lambda x: x,[True, True, False, True])))