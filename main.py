from tkinter import *
import tkinter as tk
import math
from tkinter import messagebox
window = Tk()
window.title('Change counter')

def compute():
    quarters = e1.get()
    dimes    = e2.get()
    nickels  = e3.get()
    pennies  = e4.get()

    #This code to make your application robust against negative inputs
    if(int(quarters) < 0):
        messagebox.showwarning(title="Error", message="Quarters can't have negative value!")
    elif (int(dimes) < 0):
        messagebox.showwarning(title="Error", message="Dimes can't have negative value!")
    elif (int(nickels) < 0):
        messagebox.showwarning(title="Error", message="Nickels can't have negative value!")
    elif (int(pennies) < 0):
        messagebox.showwarning(title="Error", message="Pennies value can't be negative!")
    else :
        #set value of quarters
        val1 = float(quarters) * 0.25
        e1val.delete(0,END)
        e1val.insert(0,val1)

        #set value of Dimes
        val2 = float(dimes) * 0.10
        e2val.delete(0,END)
        e2val.insert(0,val2)

        #set value of Cents 
        val3 = float(nickels) * 0.05
        e3val.delete(0,END)
        e3val.insert(0,val3)

        #set value of Pennies
        val4 = float(pennies) * 0.01
        e4val.delete(0,END)
        e4val.insert(0,val4)

        
        
        res = val1 + val2 + val3 + val4
        eresval.delete(0,END)
        eresval.insert( 0,res)
header = Label(window,text="Enter the number of each coint type and hit, Compute:")
header.grid(row = 0,columnspan=4)
Label(window, text="Quarters").grid(row=1,column=0,padx=10,pady=5)
e1 = tk.Entry(window, bd=3)
e1.grid(row=1,column = 1,padx=10,pady=5)
Label(window, text="Quarters value: $").grid(row=1,column=2,padx=10,pady=5)
e1val = tk.Entry(window, bd=3)
e1val.grid(row=1,column = 3,padx=10,pady=5)

Label(window, text="Dimes").grid(row=2,column=0,padx=10)
e2 = Entry(window, bd=3)
e2.grid(row=2,column = 1,padx=10,pady=5)
Label(window, text="Dimes value: $").grid(row=2,column=2,padx=10)
e2val = Entry( window,bd=3)
e2val.grid(row=2,column = 3,padx=10,pady=5)

Label(window, text="Nickels").grid(row=3,column=0,padx=10)
e3 = Entry(window, bd=3)
e3.grid(row=3,column = 1,padx=10,pady=5)
Label(window, text="Nickels value: $").grid(row=3,column=2,padx=10)
e3val = Entry(window, bd=3)
e3val.grid(row=3,column = 3,padx=10,pady=5)

Label(window, text="Pennis").grid(row=4,column=0,padx=10)
e4 = Entry( window,bd=3)
e4.grid(row=4,column = 1,padx=10,pady=5)
Label(window, text="Pennis value: $").grid(row=4,column=2,padx=10)
e4val = Entry(window, bd=3)
e4val.grid(row=4,column = 3,padx=10,pady=5)

Label(window, text="Total Change value: $").grid(row=5,column=2,padx=10)
tk.Button(window,text = "Compute",width = 20,command=lambda:compute()).grid(row = 5,column =0,columnspan=2)
eresval = Entry( window,bd=3)
eresval.grid(row=5,column = 3,padx=10,pady=5)

window.mainloop()



#,command = printInput to print data
