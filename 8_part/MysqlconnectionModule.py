import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root_pass",
    database='myGBdatabase')

mycursor = mydb.cursor()
def LoadFromSQL(tbl_name = 'Office'):
    mycursor.execute("SELECT * FROM Office")
    data = mycursor.fetchall()
    result = []
    for row in data:
        result.append(list(row))
    return result
print(LoadFromSQL(tbl_name = 'Office'))