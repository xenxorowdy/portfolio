from tkinter import *
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
g=Label(window, text = "Student",  background = 'green', foreground ="white",font=("Times New Roman",15)).grid(row = 0, column = 1)
a = Label(window ,text = "First Name").grid(row = 1,column = 0)
b = Label(window ,text = "Last Name").grid(row = 2,column = 0)
c = Label(window ,text = "Department").grid(row = 3,column = 0)
d = Label(window ,text = "Date of Brith").grid(row =4,column = 0)
e = Label(window,text="Roll No.").grid(row=5,column=0)
a1 = Entry(window).grid(row = 1,column = 1)
b1 = Entry(window).grid(row = 2,column = 1)
e1 = Entry(window).grid(row = 5,column=1)
btn = ttk.Button(window ,text="delete").grid(row=7,column=3)
btn1 = ttk.Button(window,text="Save").grid(row=7,column=0)
btn2=ttk.Button(window,text="Close").grid(row=7,column=1)
btn3=ttk.Button(window,text="display").grid(row=7,column=2)
n = tk.StringVar()
g =tk.IntVar()
y=tk.IntVar()
f=tk.IntVar()
dep=ttk.Combobox(window,textvariable = n) 
date=ttk.Combobox(window,textvariable = g,width=5) 
month=ttk.Combobox(window,textvariable=f,width = 4) 
year=ttk.Combobox(window,textvariable=y,width = 6) 
dep['values'] = ('Information Tecnology','Computer Science','Mechanical Engineering','Electical Engineering','Civil Engineering') 
month['value']=(list(range(1,13)))
year['value']=(list(range(1950,2020)))
date['value']=(list(range(1,32)))
dep.grid(row=3,column=1)
date.grid(row=4,column=1)
month.grid(row=4,column=2)
year.grid(row=4,column=3)
dep.current(0)
window.mainloop()