import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root_pass",
    database='myGBdatabase'
)

mycursor = mydb.cursor()


def CreateDb(db_name='myGBdatabase'):
    """ initiate new DB """
    mycursor.execute(f"CREATE DATABASE {db_name}")

def ShowDB():
    # show databases
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
      print(x)

def ShowTables():
    # show tables
    mycursor.execute("SHOW TABLES")
    tables_list = [x[0] for x in mycursor]
    for table_name in tables_list:
        print(f'Table <{table_name}>: {ShowColumns(tbl_name=table_name)}')

def ShowColumns(tbl_name='Employees'):
    mycursor.execute(f"SHOW COLUMNS FROM {tbl_name}")
    columns_list = [x[0] for x in mycursor]
    return columns_list

def MakeTable(tbl_name='New Table'):
    # make new table
    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {tbl_name} (name VARCHAR(255), address VARCHAR(255))")

def AddCol(tbl_name='Employees', tbl_column='id', col_type='INT AUTO_INCREMENT PRIMARY KEY', col_after='name'):
    """ create column in table """
    if col_after == 'FIRST':
        mycursor.execute(f'ALTER TABLE {tbl_name} ADD COLUMN {tbl_column} {col_type} {col_after}')
    else:
        mycursor.execute(f'ALTER TABLE {tbl_name} ADD COLUMN {tbl_column} {col_type} AFTER {col_after}')

def AddFrgnKeyCol(tbl_name = 'Employees',
                  tbl_column='id',
                  col_type='INT AUTO_INCREMENT PRIMARY KEY',
                  col_after='name',
                  frgn_table='Departments',
                  frgn_column='department_id'):
    """ make new column and  change it to foreign key """
    mycursor.execute(f'ALTER TABLE {tbl_name} ADD COLUMN {tbl_column} {col_type} AFTER {col_after}')
    # add new column department_id in Emploees and change column to foreign key
    mycursor.execute(f'ALTER TABLE {tbl_name} '
                     f'ADD CONSTRAINT {frgn_column} '
                     f'FOREIGN KEY ({frgn_column}) REFERENCES {frgn_table}({frgn_column}) '
                     'ON DELETE CASCADE')

def ModCol(tbl_name='Employees', tbl_column='name', col_type='VARCHAR(255)'):
    """ modify column type """
    mycursor.execute(f'ALTER TABLE {tbl_name} MODIFY {tbl_column} {col_type}')

def InitDB():
    """ Initializing tables and columns in the SQL BASE """
    # MakeTable(tbl_name='Departments')
    # AddCol(tbl_name='Departments', tbl_column='department_id', col_type='INT AUTO_INCREMENT PRIMARY KEY', col_after='FIRST')
    # AddFrgnKeyCol(tbl_name='Departments', tbl_column='manager_id', col_type='INT', col_after='department_id', frgn_table='Managers', frgn_column='manager_id')

    # MakeTable(tbl_name='Managers')
    # AddCol(tbl_name='Managers', tbl_column='manager_id', col_type='INT AUTO_INCREMENT PRIMARY KEY', col_after='FIRST')
    # mycursor.execute(f'ALTER TABLE Managers RENAME COLUMN address TO room')  # rename column

    # MakeTable(tbl_name='Office')
    # AddCol(tbl_name='Office', tbl_column='floor', col_type='INT', col_after='name')
    # mycursor.execute(f'ALTER TABLE Office RENAME COLUMN name TO room')  # rename column

    # MakeTable(tbl_name='Employees')
    # AddCol(tbl_name='Employees', tbl_column='id', col_type='INT AUTO_INCREMENT PRIMARY KEY', col_after='FIRST')
    # AddCol(tbl_name='Employees', tbl_column='phone', col_type='VARCHAR(32)', col_after='name')
    # ModCol(tbl_name='Employees', tbl_column='address', col_type='VARCHAR(255)')
    # mycursor.execute(f'ALTER TABLE Employees MODIFY address VARCHAR(255) AFTER phone') #changes col placement
    # AddCol(tbl_name='Employees', tbl_column='room', col_type='VARCHAR(255)', col_after='address')
    # AddCol(tbl_name='Employees', tbl_column='is_manager', col_type='BOOLEAN', col_after='name')
    # mycursor.execute(f'ALTER TABLE Employees DROP COLUMN is_manager')  # delete column
    # AddFrgnKeyCol(tbl_name='Employees', tbl_column='department_id', col_type='INT', col_after='name')
    # AddFrgnKeyCol(tbl_name='Employees', tbl_column='manager_id', col_type='INT', col_after='name', frgn_table='Managers', frgn_column='manager_id')

    ShowTables()

InitDB()

if '__name__' == '__main__':
    InitDB()