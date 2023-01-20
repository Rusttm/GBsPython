import tkinter as tk


master = tk.Tk()
tk.Label(master, text="First Name:").grid(row=0)
tk.Label(master, text="Last Name:").grid(row=1)
tk.Label(master, text="Phone:").grid(row=2)
tk.Label(master, text="Description:").grid(row=3)

name = tk.Entry(master)
lastname = tk.Entry(master)
phone = tk.Entry(master)
description = tk.Entry(master)

name.grid(row=0, column=1)
lastname.grid(row=1, column=1)
phone.grid(row=2, column=1)
description.grid(row=3, column=1)


def ShowFields():
    top = tk.Toplevel()
    top.geometry("150x120")
    top.title("Saved!")
    tk.Label(top, text=name.get(), font=('helvetica', 14)).grid(row=0)
    tk.Label(top, text=lastname.get(), font=('helvetica', 14)).grid(row=1)
    tk.Label(top, text=phone.get(), font=('helvetica', 14)).grid(row=2)
    tk.Label(top, text=description.get(), font=('helvetica', 14)).grid(row=3)
    tk.Button(top, text='Ok', command=top.destroy).grid(row=4)



tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=4,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Save', command=ShowFields).grid(row=4,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)


master.mainloop()



# canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
# canvas1.pack()
#
# label1 = tk.Label(root, text='Фамилия:')
# label1.config(font=('helvetica', 14))
# canvas1.create_window(200, 15, window=label1)
#
# name_entry = tk.Entry(root)
# canvas1.create_window(200, 35, window=name_entry)
#
# label2 = tk.Label(root, text='Имя:')
# label2.config(font=('helvetica', 10))
# canvas1.create_window(200, 30, window=label2)
#
#
# entry2 = tk.Entry(root)
# canvas1.create_window(200, 160, window=entry2)


# def get_square_root():
#     x1 = entry1.get()
#
#     label3 = tk.Label(root, text='The Square Root of ' + x1 + ' is:', font=('helvetica', 10))
#     canvas1.create_window(200, 210, window=label3)
#
#     label4 = tk.Label(root, text=float(x1) ** 0.5, font=('helvetica', 10, 'bold'))
#     canvas1.create_window(200, 230, window=label4)
#
#
# button1 = tk.Button(text='Get the Square Root', command=get_square_root, bg='brown', fg='white',
#                     font=('helvetica', 9, 'bold'))
# canvas1.create_window(200, 190, window=button1)
#
# root.mainloop()