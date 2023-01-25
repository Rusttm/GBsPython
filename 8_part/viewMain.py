import tkinter as tk
import viewDep

main = tk.Tk()
main.title("Employees")

def NewDepWin():
    new_window = viewDep.DepWindows()



quit_button = tk.Button(main, text='Quit', command=main.quit)
dep_button = tk.Button(main, text='Departments', command=NewDepWin)

dep_button.grid(row=4, column=0)
quit_button.grid(row=5, column=0)

main.mainloop()