# списке из строк найти, есть ли данное число

list = ['23','456','345','078','456','234','65476','7099789','2453','45674']

x =input('Задайте число')
result = 'No'
for elem in list:
    if len(elem)>len(x):
        for i in range(len(elem)-len(x)+1):
            y = elem[i:i+len(x)]
            if y == x:
                result = 'Yes'+ elem
                print(result)
                exit()
    elif elem==x:
        result = 'Yes'
        print(result)
        exit()
else:
    result = 'No'
    print(result)