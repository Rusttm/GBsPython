import csv
import json
import random

path_csv_file = 'phonebook.csv'
path_json_file = 'phonebook.json'
def LoadFromCsv():
    database = [['Id', 'Name', 'Surname', 'Phone', 'Descr']]
    with open(path_csv_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row:
                database.append(row)
    return database

def Add2Csv(data):
    with open(path_csv_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        writer.writerow([])
    return True

def Add2Json(data):
    database = {'Name': 'Name', 'Surname': 'Surname', 'Phone': 'Phone', 'Descr': 'Descr'}
    result = dict()

    for row in data:
        key = random.randint(100, 10000)
        result[key] = dict(zip(database, row))
        print(result)

    # with open(path_json_file, 'w') as file:
    #
    #
    #     writer = csv.writer(file)
    #     writer.writerow(data)
    #     writer.writerow([])
    return True

def AddData(data):
    Add2Csv(data)

def LoadData():
    return LoadFromCsv()

# def ConverterCsv2Json():

Add2Json([['My_Name', 'My_Surname', 'My_Phone', 'My_Descr'], ['No_Name', 'No_Surname', 'No_Phone', 'No_Descr']])