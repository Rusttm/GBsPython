# принимает на вход дробь, печатает первую цифру дробной части

n = float(input('Enter the Number '))

def DecimalDigitPrint(n):
    if (n<0): n =-n
    decimal_digits = n - n//1
    if (decimal_digits == 0): 
        print(f' No decimal symbols')
        return
    decimal_digit = (decimal_digits * 10) //1
    print(f' Forcs decimal symbol is {int(decimal_digit)}')

DecimalDigitPrint(n)