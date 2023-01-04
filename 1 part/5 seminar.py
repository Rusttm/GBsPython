# проверяет кратность 5,10,15 но не 30


n = int(input('Enter the Number '))

def MultChecker(n):

    if ( not(n%5 and n%10 and n%15) and (n%30)):
        print('Ok')
    else:
        print('False')

MultChecker(n)