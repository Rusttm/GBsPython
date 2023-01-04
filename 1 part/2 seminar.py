# максимальное из 5 чисел


def MaxFunction():
    input_array = []
    max_num = float('-inf')
    for i in range(5):
        input_num = int(input(f'Enter number {i} '))
        if max_num < input_num:
            max_num = input_num
        input_array.append(input_num) 
    
    print(input_array)
    print(f'максимальное число -{max_num}')

MaxFunction()