import mysql.connector
import DataTransfer
import random

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root_pass",
    database='myGBdatabase')

mycursor = mydb.cursor()
def FillDataManagers():
    rooms_list = GetColFromTbl(tbl_name='Office', column='room',  condition="floor=4")
    managers_list = DataTransfer.DataFromTitanic(user='manager', n=15)
    for manager in managers_list:
        room = rooms_list[random.randint(1, 14)]
        print(f"('{manager}, {room}' )")
        FillTblData(tbl_name='Managers', tbl_scheme='(name, room)', data=f"('{manager}', '{room}' )")
    # mydb.commit()

def FillDataDepartments():
    dep_list = ['Sales', 'Supply', 'Transport', 'Storage', 'Purchases', 'Tech', 'Finance']
    office_dict = {'Podolsk': ['Supply', 'Storage'], 'Moscow1': ['Sales', 'Transport', 'Purchases', 'Tech', 'Finance']}
    managers_ids_list = GetColFromTbl(tbl_name='Managers', column='manager_id',  condition=False)

    for address, deps in office_dict.items():
        for dep in deps:
            manager_id = random.choice(managers_ids_list)[0]
            print(f"('{manager_id}', '{dep}, '{address}')")
            FillTblData(tbl_name='Departments', tbl_scheme='(manager_id, name, address)', data=f"('{manager_id}', '{dep}', '{address}')")
    # mydb.commit()

def FillDataEmployees():
    rooms_list = GetColFromTbl(tbl_name='Office', column='room,floor',  condition="floor<4")
    users_list = DataTransfer.DataFromTitanic(user='user', n=500)
    managers_ids_list = GetColFromTbl(tbl_name='Managers', column='manager_id', condition=False)
    deps_list = GetColFromTbl(tbl_name='Departments', column='department_id, address', condition=False)

    for user in users_list:
        user = user.replace("'", "")

        manager_id = random.choice(managers_ids_list)[0]
        dep = random.choice(deps_list)
        dep_id = dep[0]
        address = dep[1]
        room = random.choice(rooms_list)
        room_no = room[0]
        phone = random.randint(1000000, 10000000)
        print(f"('{user=}, {manager_id=}, {dep_id=}, {phone=}, {address=}, {room_no=}')")
        FillTblData(tbl_name='Employees',
                    tbl_scheme='(name, manager_id, department_id, phone, address, room)',
                    data=f"('{user}', '{manager_id}', '{dep_id}', '{phone}', '{address}', '{room_no}')")
        # break
    # mydb.commit()


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
        result.append(list(x))
    return result

def FullFillAll():
    # ClearTblData(tbl_name = 'Office')
    # FillDataOffice()
    # print(GetColFromTbl(tbl_name = 'Office', column ='room',  condition = "floor=4"))
    # FillDataManagers()
    # FillDataDepartments()
    # FillDataEmployees()

if '__name__' == '__main__':
    FullFillAll()
