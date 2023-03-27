from tkinter import *

root = Tk()
root.title("simple caculator")

e = Entry(root,width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
     e.delete(0,END)
     
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "substraction":
        e.insert(0, f_num - int(second_number))
    if math == "mutiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
       
    
def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "mutiplication"
    f_num = int(first_number)
    e.delete(0,END) 
  

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END) 

button_01 = Button(root, text="1", padx=50, pady=20, command= lambda: button_click(1))
button_02 = Button(root, text="2", padx=50, pady=20, command= lambda: button_click(2))
button_03 = Button(root, text="3", padx=50, pady=20, command= lambda: button_click(3))
button_04 = Button(root, text="4", padx=50, pady=20, command= lambda: button_click(4))
button_05 = Button(root, text="5", padx=50, pady=20, command= lambda: button_click(5))
button_06 = Button(root, text="6", padx=50, pady=20, command= lambda: button_click(6))
button_07 = Button(root, text="7", padx=50, pady=20, command= lambda: button_click(7))
button_08 = Button(root, text="8", padx=50, pady=20, command= lambda: button_click(8))
button_09 = Button(root, text="9", padx=50, pady=20, command= lambda:  button_click(9))
button_00 = Button(root, text="0", padx=50, pady=20, command= lambda: button_click(0))

button_add = Button(root, text="+", padx=49, pady=20, command= button_add)
button_clear = Button(root, text="Clear", padx=100, pady=20, command= button_clear)
button_equal = Button(root, text="=", padx=110, pady=20, command= button_equal)

button_substract = Button(root, text="-", padx=50, pady=20, command= button_substract)
button_multiply = Button(root, text="×", padx=50, pady=20, command= button_multiply)
button_divide = Button(root, text="÷", padx=50, pady=20, command= button_divide)

button_01.grid(row=3 , column=0)
button_02.grid(row=3 , column=1)
button_03.grid(row=3 , column=2)


button_04.grid(row=2 , column=0)
button_05.grid(row=2 , column=1)
button_06.grid(row=2 , column=2)


button_07.grid(row=1 , column=0)
button_08.grid(row=1 , column=1)
button_09.grid(row=1 , column=2)

button_00.grid(row=4 , column=0)
button_clear.grid(row=4 , column=1, columnspan=2)
button_add.grid(row=5 , column=0)
button_equal.grid(row=5 , column=1, columnspan=2)


button_substract.grid(row=6 , column=0)
button_multiply.grid(row=6 , column=1)
button_divide.grid(row=6 , column=2)

root.mainloop() 
