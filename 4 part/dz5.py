# 5 Даны два файла, в каждом из которых 
# находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# считываем из 1 файла уравнение
with open('dz5_1_file.txt', 'r') as f:
    equation_string_1 = f.readline()

# считываем из 2 файла уравнение
with open('dz5_2_file.txt', 'r') as f:
    equation_string_2 = f.readline()

print(equation_string_1)
print('+')
print(equation_string_2)
print('=>')

def Transform2Eq(equation_string: str):
    ''' преобразует строку '8*x**3 + 38*x**2 + 94*x = 0' в словарь вида {степень:коэф, }'''
    # переводим строки в списки
    eq_list = equation_string.replace('=','+').split(' + ')[:-1]
    result_dict = dict()
    for elem in eq_list:
        elem_splitted = elem.split('*x**')
        if (len(elem_splitted) == 2):
            coef = int(elem_splitted[0])
            range = int(elem_splitted[1])
        else:
            elem_splitted = elem.split('*x')
            if (len(elem_splitted) == 2):
                coef = int(elem_splitted[0])
                range = 1
            else:
                coef = int(elem)
                range = 0
        result_dict[range] = coef
    

    return result_dict

def SummEquations(equation_string_1, equation_string_2):
    '''суммирует коэфициенты при степенях и выдает словарь'''
    eq1_dict = Transform2Eq(equation_string_1)
    eq2_dict = Transform2Eq(equation_string_2)
    # ищем выражение с максимальной степенью
    max_range = max(max(eq1_dict.keys()),max(eq2_dict.keys()))
    result_dict = dict()
    for r in range(max_range+1):
        result_dict[r] = eq1_dict.get(r,0) + eq2_dict.get(r,0)
    return result_dict

def PrintDict(result_dict):
    '''распечатывает уравнение, заданное словарем {степень:коэфициент}'''
    max_range = max(result_dict.keys())
    result_string = ''
    for i in range(max_range,1,-1):
        if (result_dict[i] != 0):
            coef = result_dict[i]
            result_string += f'{coef}*x**{i}'
            if (result_dict[i-1]!=0):
                result_string += ' + '
    if (result_dict[1] != 0):
        coef = result_dict[1]
        result_string += f'{coef}*x'
        if (result_dict[0]!=0):
                result_string += ' + '
    if (result_dict[0] != 0):
        coef = result_dict[0]
        result_string += f'{coef}'
    result_string += ' = 0'
    print(result_string)

PrintDict(SummEquations(equation_string_1, equation_string_2))
