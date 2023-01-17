# вычисление арифметического выражения
# 2 + 1 + 3 * 4 * 2 + 6 / 3 => 29
# со скобками
# 2 + ( 1 + 3 ) * ( 1 + 1 + 2 ) * ( 2 + 6 / 3 ) => 66
# ( 2 + ( 1 + 3 ) ) * ( 1 + 1 + 2 ) * ( 2 + 6 / 3 ) => 96
# ( 2 + ( 1 + 3 ) ) * ( 1 + 1 + 2 ) - ( 7 + 6 * 2 / 3 ) => 13


s = input('Введите выражение: ')
def EqReader(s: str) -> list:
    string_list = s.split()
    return string_list


def CalcList(expr_list: list) -> str:
    result = 0
    expressions = ['/', '*', '+', '-']
    for expr in expressions:
        while expr_list.count(expr)!=0:
            i = expr_list.index(expr)
            a = expr_list.pop(i-1)
            x = expr_list.pop(i-1)
            b = expr_list.pop(i-1)
            expr_list.insert(i-1, CalcTwo(a,x,b))
    return ''.join(expr_list)


def CalcHooks(expr_list: list) -> float:
    left_hook = 0
    right_hook = 0
    inner_expression = []
    while expr_list.count('(')!=0:
        inner_expression = []
        right_hook = expr_list.index(')')
        expr_list.pop(right_hook)
        for i in range(right_hook -1, -1, -1):
            elem = expr_list.pop(i)
            if elem == '(':
                left_hook = i
                break
            else:
                inner_expression.insert(0, elem)
        expr_list.insert(left_hook, CalcList(inner_expression))  
    return CalcList(expr_list)
            

def CalcTwo(a:str,x:str,b:str) -> float:
    if x == '/':
        return str(float(a)/float(b))
    if x == '*':
        return str(float(a)*float(b))
    if x == '+':
        return str(float(a)+float(b))
    if x == '-':
        return str(float(a)-float(b))


print(CalcHooks(EqReader(s)))

    
