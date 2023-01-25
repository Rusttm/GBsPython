import pandas as pd
from sklearn.model_selection import train_test_split
# import sklearn
# print(sklearn.__version__)


def DataFromTitanic(user='user', n=100):
    data_csv = '/Users/johnlennon/Downloads/titanic.csv'
    data = pd.read_csv(data_csv)
    user_data, manager_data = train_test_split(data, test_size=0.2, random_state=77)
    result = []
    if user == 'user':
        for i in range(n):
            result.append(user_data['Name'].iloc[i])
    elif user == 'manager':
        for i in range(n):
            result.append(manager_data['Name'].ilo[i])
    else:
        return []
    return result


if '__name__' == '__main__':
    print(DataFromTitanic(user='user', n = 10))
