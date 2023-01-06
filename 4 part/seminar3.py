# НОК двух чисел


a = int(input('Enter a: '))
b = int(input('Enter b: '))



def Nok(a,b):
    mx, mn = max(a,b), min(a,b)
    for n in range(mx, mx*mn):
        if (n%mn == 0) and n%mx == 0:
            return n
    return mx*mn

print(Nok(a,b))