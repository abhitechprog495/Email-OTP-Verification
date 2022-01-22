#Import necessary modules and libraries
import os
from tkinter import *
from tkinter import messagebox

#Initialize the window
root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Email OTP")

#Function to verify and proceed to mail
def take_email():
    cmd=str(a.get())
    temp='python sendmail.py'+' '+cmd
    os.system(temp)

#Label entry field and button
label1=Label(root,text="One Time Password",font="arial 26 bold",fg="black")
label1.place(x=83,y=30)
a=StringVar()
Re=Label(root,text="Email Id",font="arial 16 bold").place(x=20,y=106)
w=Entry(root,width=60,validate="key",textvariable=a)
w.place(x=120,y=110)
log = Button(root,text="PROCEED",bg='LimeGreen',font="arial 20",fg='black',command=take_email)
log.place(x=180,y=180)
root.mainloop()