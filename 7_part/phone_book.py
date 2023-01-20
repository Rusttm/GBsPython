'''
программа имеет GUI интерфейс для внесения и просмотра записей в телефонную книгу
при этом запись и чтение осуществляются в модуле dbmodule.py
в котором независимо устанавливается параметры записи (формат файла)
'''


import tkinter as tk
import random
import dbmodule

# initiate tkinter fields
master = tk.Tk()

# объявляем надписи
id_sign = tk.Label(master, text="Id:")
id_label = tk.Label(master, text="0")
name_label = tk.Label(master, text="First Name:")
surname_label = tk.Label(master, text="Last Name:")
phone_label = tk.Label(master, text="Phone:")
description_label = tk.Label(master, text="Description:")

# объявляем поля для ввода данных
name = tk.Entry(master)
lastname = tk.Entry(master)
phone = tk.Entry(master)
description = tk.Entry(master)


# размещаем по полю
id_sign.grid(row=0)
id_label.grid(row=0, column=1)
name_label.grid(row=1)
surname_label.grid(row=2)
phone_label.grid(row=3)
description_label.grid(row=4)

name.grid(row=1, column=1)
lastname.grid(row=2, column=1)
phone.grid(row=3, column=1)
description.grid(row=4, column=1)

# объявляем переменные
database = [['Id', 'Name', 'Surname', 'Phone', 'Descr']]
current_pos = [0,0] # current_pos[0] - номер текущей позиции


# functions pack
def SaveFields():
    ''' записываем в файл path_csv_file = phonebook.csv '''
    current_id = random.randint(100, 10000)
    id_label.config(text=current_id)
    current_name = name.get()
    current_lastname = lastname.get()
    current_phone = phone.get()
    current_description = description.get()
    if len(current_name) != 0 and len(current_lastname) != 0 and len(current_phone) != 0 and len(current_description) != 0:
        data = [current_id, current_name, current_lastname, current_phone, current_description]
        dbmodule.AddData(data)
        info_text = "Saved!"
    else:
        info_text = "Error! Not filled"
    top = tk.Toplevel()
    top.geometry("180x180")
    top.title(info_text)

    tk.Label(top, text=current_id).grid(row=0)
    tk.Label(top, text=current_name, font=('helvetica', 14)).grid(row=1)
    tk.Label(top, text=current_lastname, font=('helvetica', 14)).grid(row=2)
    tk.Label(top, text=current_phone, font=('helvetica', 14)).grid(row=3)
    tk.Label(top, text=current_description, font=('helvetica', 14)).grid(row=4)

    tk.Button(top, text='Ok', command=top.destroy).grid(row=5)

def ClearFields():
    '''очищает поля'''
    id_label.config(text='')
    # id_label.text() = ''
    name.delete(0, tk.END)
    lastname.delete(0, tk.END)
    phone.delete(0, tk.END)
    description.delete(0, tk.END)

def LoadFields():
    '''вызывается по кнопке Load и из файла загружает в
    базу для использования в программе'''
    global database
    global current_pos
    database = [['Id', 'Name', 'Surname', 'Phone', 'Descr']]
    current_pos = [0, 0]
    database = dbmodule.LoadData()
    current_pos[1] = len(database)

def NextFields():
    '''вызывается по кнопке Next и из файла записывает в поля'''
    global current_pos
    global database
    if current_pos[0] >= current_pos[1]:
        current_pos[0] = 0

    ClearFields()
    id_label.config(text=database[current_pos[0]][0])
    name.insert(0, database[current_pos[0]][1])
    lastname.insert(0, database[current_pos[0]][2])
    phone.insert(0, database[current_pos[0]][3])
    description.insert(0, database[current_pos[0]][4])
    current_pos[0] += 1


# buttons pack
tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=5,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Save', command=SaveFields).grid(row=5,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

# next buttons line

tk.Button(master,
          text='Clear', command=ClearFields).grid(row=6,
                                                       column=0,
                                                       sticky=tk.W,
                                                       pady=4)
tk.Button(master,
          text='Load', command=LoadFields).grid(row=6,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.Button(master,
          text='Next', command=NextFields).grid(row=6,
                                                  column=2,
                                                  sticky=tk.W,
                                                    pady=4)




master.mainloop()

