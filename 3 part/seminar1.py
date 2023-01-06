# сделать генератор псевдослучайных чисел

from datetime import datetime

number = float(datetime.now().strftime("%s"))%100000
random_number = float(number)%2 + float(number)%3*10 + float(number)%7*10
print(number)
print(random_number)