import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_pass",
    database='myGBdatabase'
)

mycursor = mydb.cursor()

# make new DB
# mycursor.execute("CREATE DATABASE myGBdatabase")


def ShowDB():
    # show databases
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
      print(x)


def MakeTable(tbl_name='New Table'):
    # make new table
    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {tbl_name} (name VARCHAR(255), address VARCHAR(255))")

def ShowTables():
    # show tables
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
      print(x)

def AddCol(tbl_name = 'Employees', tbl_column = 'id', col_type = 'INT AUTO_INCREMENT PRIMARY KEY', col_after = 'name'):
    '''create column in table'''
    if col_after == 'FIRST':
        mycursor.execute(f'ALTER TABLE {tbl_name} ADD COLUMN {tbl_column} {col_type} {col_after}')
    else:
        mycursor.execute(f'ALTER TABLE {tbl_name} ADD COLUMN {tbl_column} {col_type} AFTER {col_after}')

def AddFrgnKeyCol(tbl_name = 'Employees',
                  tbl_column = 'id',
                  col_type = 'INT AUTO_INCREMENT PRIMARY KEY',
                  col_after = 'name',
                  frgn_table = 'Departments',
                  frgn_column = 'department_id'):
    ''' make new column and  chenge it to foreign key '''
    mycursor.execute(f'ALTER TABLE {tbl_name} ADD COLUMN {tbl_column} {col_type} AFTER {col_after}')
    # add new column department_id in Emploees and change column to foreign key
    mycursor.execute(f'ALTER TABLE {tbl_name} '
                     f'ADD CONSTRAINT {frgn_column} '
                     f'FOREIGN KEY ({frgn_column}) REFERENCES {frgn_table}({frgn_column}) '
                     'ON DELETE CASCADE')

    #create

def ModCol(tbl_name = 'Employees', tbl_column = 'name', col_type = 'VARCHAR(255)', col_after = 'name'):
    # modify column
    mycursor.execute(f'ALTER TABLE {tbl_name} MODIFY {tbl_column} {col_type}')


    #create


def ModTable(tbl_name = 'Employees', tbl_column = 'id'):
    pass


# Initializing and FILL the SQL BASE
# MakeTable(tbl_name='Departments')
# MakeTable(tbl_name='Managers')
# MakeTable(tbl_name='Employees')
# AddCol(tbl_name='Employees', tbl_column='id', col_type='INT AUTO_INCREMENT PRIMARY KEY', col_after='FIRST')
# AddCol(tbl_name='Departments', tbl_column='department_id', col_type='INT AUTO_INCREMENT PRIMARY KEY', col_after='FIRST')
# AddCol(tbl_name='Managers', tbl_column='manager_id', col_type='INT AUTO_INCREMENT PRIMARY KEY', col_after='FIRST')
# AddFrgnKeyCol(tbl_name='Employees', tbl_column='department_id', col_type='INT', col_after='name')
# AddFrgnKeyCol(tbl_name='Employees', tbl_column='manager_id', col_type='INT', col_after='name', frgn_table='Managers', frgn_column='manager_id')
# AddFrgnKeyCol(tbl_name='Departments', tbl_column='manager_id', col_type='INT', col_after='department_id', frgn_table='Managers', frgn_column='manager_id')

# AddCol(tbl_name='Employees', tbl_column='manager_id', col_type='INT FOREIGN KEY', col_after='department_id')

ShowTables()