#Simple calculator

from tkinter import *
import tkinter
import tkinter.messagebox



def calculation():
    try:
        number_1=Entry.get(E1)
        number_2=Entry.get(E2)
        operator=Entry.get(E3)
        number1=int(number_1)
        number2=int(number_2)
        if operator =="+":
            answer=number1+number2
        if operator =="-":
            answer=number1-number2
        if operator=="*":
            answer=number1*number2
        if operator=="/":
            answer=number1/number2
        Entry.insert(E4,0,answer)
        print(answer)

    except ValueError:
        tkinter.messagebox.showinfo("Warning",'Please Enter correct value')

#GUI code
top = tkinter.Tk()
L1 = Label(top, text="CALCULATOR",).grid(row=0,column=1)
L2 = Label(top, text="1.Number",).grid(row=1,column=0)
L3 = Label(top, text="2.Number",).grid(row=2,column=0)
L4 = Label(top, text="Operator",).grid(row=3,column=0)
L4 = Label(top, text="Result",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = calculation).grid(row=5,column=1,)

top.mainloop()
