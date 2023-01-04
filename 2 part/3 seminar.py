# количество вхождений одной строки в другую

string1 = input('Введите строку: ')
string2 = input('Введите строку поиска: ')

def FindString(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    count = 0
    for i in range(len1):
        if (string1[i:i+len2]==string2):
            count +=1
    print(count)


FindString(string1, string2)