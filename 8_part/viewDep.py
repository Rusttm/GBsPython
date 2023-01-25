""" модуль для графического вывода данных из Department"""

import tkinter as tk

# initiate tkinter fields
dep = tk.Tk()

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
id_name = tk.Label(dep, text="")
manager_name = tk.Entry(dep)
dep_name = tk.Entry(dep)
dep_address_name = tk.Entry(dep)
# размещаем ввод по полю
id_name.grid(row=0, column=1)
manager_name.grid(row=1, column=1)
dep_name.grid(row=2, column=1)
dep_address_name.grid(row=3, column=1)

dep.mainloop()