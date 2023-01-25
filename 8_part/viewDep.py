""" модуль для графического вывода данных из Department"""

import tkinter as tk
import MysqlconnectionModule


class DepWindows:

    def __init__(self):
        self.data = MysqlconnectionModule.LoadFromSQL(tbl_name='Departments')
        self.current_pos = [0, len(self.data)-1]
        print(self.data)
        self.DepCanvas()

    def ClearFields(self):
        self.id_name.config(text="0")
        self.manager_name.delete(0, tk.END)
        self.dep_name.delete(0, tk.END)
        self.dep_address_name.delete(0, tk.END)
    def PrevPosition(self):
        if self.current_pos[0] == 0:
            self.current_pos[0] = self.current_pos[1]
        else:
            self.current_pos[0] -= 1

        i = self.current_pos[0]
        self.ClearFields()
        self.id_name.config(text=self.data[i][0])
        mangr_id = self.data[i][1]
        manager = MysqlconnectionModule.LoadCrossFromSQL(select='name', value=mangr_id,
                                                         tbl1_name='Departments', field1='manager_id',
                                                         tbl2_name='Managers', field2='manager_id')

        self.manager_name.insert(0, manager[0][1])
        self.dep_name.insert(0, self.data[i][2])
        self.dep_address_name.insert(0, self.data[i][3])
    def NextPosition(self):
        if self.current_pos[0] == self.current_pos[1]:
            self.current_pos[0] = 0
        else:
            self.current_pos[0] += 1
        self.ClearFields()
        i = self.current_pos[0]
        self.id_name.config(text=self.data[i][0])

        mangr_id = self.data[i][1]
        manager = MysqlconnectionModule.LoadCrossFromSQL(select='name', value=mangr_id,
                                                         tbl1_name='Departments', field1='manager_id',
                                                         tbl2_name='Managers', field2='manager_id')
        self.manager_name.insert(0, manager[0][1])

        self.dep_name.insert(0, self.data[i][2])
        self.dep_address_name.insert(0, self.data[i][3])

    def DepCanvas(self):
        # initiate tkinter fields
        dep = tk.Tk()
        dep.title("Departments")
        # объявляем надписи
        id_label = tk.Label(dep, text="Id:")
        manager_name_label = tk.Label(dep, text="Manager")
        dep_name_label = tk.Label(dep, text="Department:")
        address_label = tk.Label(dep, text="address:")
        # размещаем надписи по полю
        id_label.grid(row=0)
        manager_name_label.grid(row=1)
        dep_name_label.grid(row=2)
        address_label.grid(row=3)

        # объявляем поля для ввода данных
        self.id_name = tk.Label(dep, text="")
        self.manager_name = tk.Entry(dep)
        self.dep_name = tk.Entry(dep)
        self.dep_address_name = tk.Entry(dep)
        # размещаем ввод по полю
        self.id_name.grid(row=0, column=1)
        self.manager_name.grid(row=1, column=1)
        self.dep_name.grid(row=2, column=1)
        self.dep_address_name.grid(row=3, column=1)

        # объявляем кнопки
        # создаем pack для размещения в одной колонке нескольких кнопок
        dep_buttons_pack1 = tk.Frame(dep)
        dep_buttons_pack2 = tk.Frame(dep)
        quit_button = tk.Button(dep, text='Quit', command=dep.quit)
        update_button = tk.Button(dep, text='Update', command=dep.quit)
        prev_button = tk.Button(dep_buttons_pack1, text='Prev', command=self.PrevPosition)
        next_button = tk.Button(dep_buttons_pack1, text='Next', command=self.NextPosition)
        new_button = tk.Button(dep_buttons_pack2, text='New', command=dep.quit)
        save_button = tk.Button(dep_buttons_pack2, text='Save', command=dep.quit)


        # размещаем кнопки на рабочей площади
        update_button.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)
        # размещаем пакеты кнопок
        dep_buttons_pack1.grid(row=4, column=1)
        dep_buttons_pack2.grid(row=5, column=1)
        # размещаем кнопки в пакетах
        prev_button.pack(side=tk.LEFT)
        next_button.pack(side=tk.RIGHT)
        new_button.pack(side=tk.LEFT)
        save_button.pack(side=tk.RIGHT)
        # update_button.pack(side=tk.TOP)

        dep.mainloop()

if '__name__' == '__main__':
    new_window = DepWindows()