import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root_pass",
    database='myGBdatabase')

mycursor = mydb.cursor()
def FillDataOffice():
    office_address = '119002, Moscow, per Denezhniy, 19'
    for floor in range(1, 5):
        for ii in range(10, 30):
            room = f'{floor}{ii}'
            FillTblData(tbl_name='Office', tbl_scheme='(room, floor, address)', data=f"('{room}', '{floor}', '{office_address}')")
    # mydb.commit()

def FillTblData(tbl_name = 'Office', tbl_scheme = '(room, floor, address)', data = "('1','2','test')"):
    mycursor.execute(f"INSERT INTO {tbl_name} {tbl_scheme} VALUES {data}")
    mydb.commit()

def ClearTblData(tbl_name = 'Office', condition = False):
    if not condition:
        mycursor.execute(f"TRUNCATE {tbl_name}")
    else:
        mycursor.execute(f"DELETE FROM {tbl_name} WHERE {condition}")
    mydb.commit()

def GetColFromTbl(tbl_name = 'Office', column ='room',  condition = False):
    result = []
    if not condition:
        mycursor.execute(f"SELECT {column} FROM {tbl_name}")
    else:
        mycursor.execute(f"SELECT {column} FROM {tbl_name} WHERE {condition}")
    my_result = mycursor.fetchall()
    for x in my_result:
        result.append(x[0])
    return result

def FullFillAll():
    # ClearTblData(tbl_name = 'Office')
    # FillDataOffice()
    # print(GetColFromTbl(tbl_name = 'Office', column ='room',  condition = "floor=4"))

FullFillAll()
