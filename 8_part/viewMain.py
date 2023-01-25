"""
программа имеет GUI интерфейс для внесения и просмотра записей в базу сотрудников
при этом запись и чтение осуществляются в модуле MysqlconnectionModule.py
база данных развернута на Docker образе и начально заполняется с помощью файлов
MysqlinitModule - инициализация
MysqlfillModule - заполнение
отдельным модулем создается окно Department
"""


import tkinter as tk
import viewDep
import MysqlconnectionModule


class MainWindow:

    def __init__(self):
        self.data = MysqlconnectionModule.LoadFromSQL(tbl_name='Employees')
        self.current_pos = [0, len(self.data)-1]
        print(self.data)
        self.MainCanvas()



    def NewDepWin(self):
        viewDep.DepWindows()

    def ClearFields(self):
        self.id_name.config(text="")
        self.user_name.delete(0, tk.END)
        self.phone_name.delete(0, tk.END)
        self.room_name.delete(0, tk.END)
        self.dep_name.delete(0, tk.END)
        self.manager_name.delete(0, tk.END)
        self.addres_name.delete(0, tk.END)


    def PrevPosition(self):
        pass
        if self.current_pos[0] == 0:
            self.current_pos[0] = self.current_pos[1]
        else:
            self.current_pos[0] -= 1

        i = self.current_pos[0]
        self.ClearFields()
        self.id_name.config(text=self.data[i][0])

        # manager_id --> manager name
        mangr_id = self.data[i][2]
        manager = MysqlconnectionModule.LoadCrossFromSQL(select='name', value=mangr_id,
                                                         tbl1_name='Employees', field1='manager_id',
                                                         tbl2_name='Managers', field2='manager_id')
        self.manager_name.insert(0, manager[0][1])


        # department_id --> department name
        dep_id = self.data[i][3]
        department = MysqlconnectionModule.LoadCrossFromSQL(select='name', value=dep_id,
                                                         tbl1_name='Employees', field1='department_id',
                                                         tbl2_name='Departments', field2='department_id')
        self.dep_name.insert(0, department[1])
        self.user_name.insert(0, self.data[i][1])
        self.phone_name.insert(0, self.data[i][4])
        self.room_name.insert(0, self.data[i][6])
        self.addres_name.insert(0, self.data[i][5])





    def NextPosition(self):
        pass
        if self.current_pos[0] == self.current_pos[1]:
            self.current_pos[0] = 0
        else:
            self.current_pos[0] += 1
        self.ClearFields()
        i = self.current_pos[0]
        self.id_name.config(text=self.data[i][0])

        # manager_id --> manager name
        mangr_id = self.data[i][2]
        manager = MysqlconnectionModule.LoadCrossFromSQL(select='name', value=mangr_id,
                                                         tbl1_name='Employees', field1='manager_id',
                                                         tbl2_name='Managers', field2='manager_id')
        self.manager_name.insert(0, manager[0][1])


        # department_id --> department name
        dep_id = self.data[i][3]
        department = MysqlconnectionModule.LoadCrossFromSQL(select='name', value=dep_id,
                                                         tbl1_name='Employees', field1='department_id',
                                                         tbl2_name='Departments', field2='department_id')
        self.dep_name.insert(0, department[1])
        self.user_name.insert(0, self.data[i][1])
        self.phone_name.insert(0, self.data[i][4])
        self.room_name.insert(0, self.data[i][6])
        self.addres_name.insert(0, self.data[i][5])

    def MainCanvas(self):
        main = tk.Tk()
        main.title("Employees")

        # объявляем надписи
        id_label = tk.Label(main, text="Id:")
        user_name_label = tk.Label(main, text="User")
        dep_name_label = tk.Label(main, text="Department:")
        room_number_label = tk.Label(main, text="Room:")
        phone_number_label = tk.Label(main, text="Phone:")
        manager_name_label = tk.Label(main, text="Manager")
        address_label = tk.Label(main, text="Address:")

        # размещаем надписи по полю
        id_label.grid(row=0)
        user_name_label.grid(row=1)
        phone_number_label.grid(row=2)
        room_number_label.grid(row=3)
        dep_name_label.grid(row=1, column=2)
        manager_name_label.grid(row=2, column=2)
        address_label.grid(row=3, column=2)

        # объявляем поля для ввода данных
        self.id_name = tk.Label(main, text="")
        self.user_name = tk.Entry(main)
        self.phone_name = tk.Entry(main)
        self.room_name = tk.Entry(main)
        self.dep_name = tk.Entry(main)
        self.manager_name = tk.Entry(main)
        self.addres_name = tk.Entry(main)

        # размещаем ввод по полю
        self.id_name.grid(row=0, column=1)
        self.user_name.grid(row=1, column=1)
        self.phone_name.grid(row=2, column=1)
        self.room_name.grid(row=3, column=1)
        self.dep_name.grid(row=1, column=3)
        self.manager_name.grid(row=2, column=3)
        self.addres_name.grid(row=3, column=3)


        # создаем кнопки
        emp_buttons_pack1 = tk.Frame(main)
        quit_button = tk.Button(main, text='Quit', command=main.quit)
        dep_button = tk.Button(main, text='Departments', command=self.NewDepWin)
        prev_button = tk.Button(emp_buttons_pack1, text='Prev', command=self.PrevPosition)
        next_button = tk.Button(emp_buttons_pack1, text='Next', command=self.NextPosition)
        # организуем кнопки
        emp_buttons_pack1.grid(row=4, column=1)
        quit_button.grid(row=4, column=0)
        dep_button.grid(row=4, column=3)
        prev_button.pack(side=tk.LEFT)
        next_button.pack(side=tk.RIGHT)


        main.mainloop()


new_window = MainWindow()