import csv
import json
import random

work_format = 'json'
csv_file = 'phonebook.csv'
json_file = 'phonebook.json'
def LoadFromCsv(path_csv_file = csv_file):
    database = [['Id', 'Name', 'Surname', 'Phone', 'Descr']]
    with open(path_csv_file, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row:
                database.append(row)
    return database

def LoadFromJson(path_json_file = json_file):
    with open(path_json_file) as json_file:
        my_data = json.load(json_file)

    result = []
    for key in my_data.keys():
        result.append([key, my_data[key]['Name'],
                       my_data[key]['Surname'],
                       my_data[key]['Phone'],
                       my_data[key]['Descr'] ])
    return result

def Add2Csv(data, path_csv_file = csv_file):
    with open(path_csv_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        writer.writerow([])
    return True

def Add2Json(data, path_json_file = json_file):
    database = ['Name', 'Surname', 'Phone', 'Descr']
    # to append data we must load current data

    with open(path_json_file) as loaded_json_file:
        json_data = json.load(loaded_json_file)

    json_data[data[0]] = dict(zip(database, data[1:]))

    with open(path_json_file, 'w') as outfile:
        json.dump(json_data, outfile)

    return True

def AddData(data, file_type = work_format):
    if file_type == 'csv':
        Add2Csv(data)
    if file_type == 'json':
        Add2Json(data)

def LoadData(file_type = work_format):
    if file_type == 'csv':
        return LoadFromCsv()
    if file_type == 'json':
        return LoadFromJson()

def ConverterCsv2Json(path_csv_file = csv_file, path_json_file = json_file):
    database = LoadFromCsv(path_csv_file)
    Add2Json(database, path_json_file)
    return True


if "__name__" == "__main__":
    data = [['My_id', 'My_Name', 'My_Surname', 'My_Phone', 'My_Descr'],
            ['No_id', 'No_Name', 'No_Surname', 'No_Phone', 'No_Descr']]
    Add2Json(data)
    print(LoadFromJson())