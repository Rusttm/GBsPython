# ищет второе вхождение строки в списке



my_list = ['23','456','345','078','456','234','65476','7099789','2453','45674']

x =input('Задайте подстроку')

def FindSecond(my_list: list, x: str):
    counter = 0
    for ii, elem in enumerate(my_list):
        if len(elem)>len(x):
            for i in range(len(elem)-len(x)+1):
                y = elem[i:i+len(x)]
                if y == x:
                    counter +=1
                    if counter == 2:
                        return f'Yes: elem[{ii}] = {elem}'
        elif elem==x:
            count += 1
            if counter == 2:
                return f'Yes: elem[{ii}] = {elem}'
    return 'No'


print(FindSecond(my_list, x))