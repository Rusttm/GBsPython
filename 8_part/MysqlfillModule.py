import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root_pass",
    database='myGBdatabase')

mycursor = mydb.cursor()
def FillDataOffice():
    tbl_name = 'Office'
    tbl_scheme = '(room, floor, address)'
    office_address = '119002, Moscow, per Denezhniy, 19'
    # mycursor.execute(f"INSERT INTO Office (room, floor, address) VALUES ('1','2','test')")
    mycursor.execute("INSERT INTO Office (room, floor, address) VALUES ('418', '4', '119002 Moscow per Denezhniy 19')")
    # for floor in range(1, 5):
    #     for ii in range(1, 20):
    #         room = f'{floor}{ii}'
    #         print(f"INSERT INTO {tbl_name} {tbl_scheme} VALUES ('{room}', '{floor}', '{office_address}')")
    #         mycursor.execute(f"INSERT INTO {tbl_name} {tbl_scheme} VALUES ('{room}', '{floor}', '{office_address}')")
    data = mycursor.fetchall()
    print(data)
FillDataOffice()