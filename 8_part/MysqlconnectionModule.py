import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root_pass",
    database='myGBdatabase')

mycursor = mydb.cursor()
def LoadFromSQL(tbl_name = 'Office'):
    mycursor.execute(f"SELECT * FROM {tbl_name}")
    data = mycursor.fetchall()
    result = []
    for row in data:
        result.append(list(row))
    return result

if '__name__' == '__main__':
    print(LoadFromSQL(tbl_name = 'Office'))