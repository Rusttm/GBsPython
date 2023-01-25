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

# объявляем кнопки
dep_buttons_pack1 = tk.Frame(dep)
dep_buttons_pack2 = tk.Frame(dep)
quit_button = tk.Button(dep, text='Quit', command=dep.quit)
update_button = tk.Button(dep, text='Update', command=dep.quit)
prev_button = tk.Button(dep_buttons_pack1, text='Prev', command=dep.quit)
next_button = tk.Button(dep_buttons_pack1, text='Next', command=dep.quit)
new_button = tk.Button(dep_buttons_pack2, text='New', command=dep.quit)
save_button = tk.Button(dep_buttons_pack2, text='Save', command=dep.quit)

# update_button = tk.Button(dep_buttons_pack2, text='Update', command=dep.quit)

# размещаем кнопки
update_button.grid(row=4, column=0)
quit_button.grid(row=5, column=0)
dep_buttons_pack1.grid(row=4, column=1)
dep_buttons_pack2.grid(row=5, column=1)

prev_button.pack(side=tk.LEFT)
next_button.pack(side=tk.RIGHT)
new_button.pack(side=tk.LEFT)
save_button.pack(side=tk.RIGHT)
# update_button.pack(side=tk.TOP)

dep.mainloop()