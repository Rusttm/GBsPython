import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root_pass",
    database='myGBdatabase')

mycursor = mydb.cursor()


def LoadFromSQL(tbl_name='Office'):
    mycursor.execute(f"SELECT * FROM {tbl_name}")
    data = mycursor.fetchall()
    result = []
    for row in data:
        result.append(list(row))
    return result


def LoadCrossFromSQL(
        select='name',
        value='1',
        tbl1_name='Departments', field1='manager_id',
        tbl2_name='Managers', field2='manager_id'):

    if value:
        command = f"SELECT * FROM (SELECT {tbl2_name}.{field2}, {tbl2_name}.{select} FROM {tbl1_name} RIGHT JOIN {tbl2_name} ON {tbl1_name}.{field1} = {tbl2_name}.{field2})tb WHERE {field2} = {value}"
    else:
        command = f"SELECT {tbl2_name}.{field2}, {tbl2_name}.{select} FROM {tbl1_name} RIGHT JOIN {tbl2_name} ON {tbl1_name}.{field1} = {tbl2_name}.{field2}"


    mycursor.execute(command)
    data = mycursor.fetchall()
    result = []
    for row in data:
        result.append(list(row))
    return result




if '__name__' == '__main__':
    print(LoadFromSQL(tbl_name='Office'))
    print(LoadCrossFromSQL())
