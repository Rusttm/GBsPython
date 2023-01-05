# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

input_string = input('Enter the Number ')

my_array = [int(s) if s not in [',','.','-'] else 0 for s in input_string]
print(f'{input_string} -> {sum(my_array)}')