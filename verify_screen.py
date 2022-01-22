#Import necessary modules and libraries
from tkinter import *
from tkinter import messagebox
import tkinter
import time
import os

#Initialize the window
#Note - This window is only revoke automatically when the OTP is mailed to the email id.
#Otherwise it need to open manually.
Window=Tk()
Window.geometry("500x300")
Window.resizable(0,0)
Window.title("Verifying.....")

#global variable for count calculation. Initially there are 3 attempts. So I set as 3
count = 3

#Function to verify the OTP
def verify():
    global count
    global Window
    end=time.time() # timers ends when the user clicks verfiy
    t = format(end - start) # calculate the difference between end and start timer
    print(float(t)) # print the time in seconds
    if float(t) >= 120: # Check it the user enters above 2 minutes. So i set as >=120
        messagebox.showinfo("Time out", "Session Expired ...Time out Please regenerate OTP")
        Window.destroy()
    else:
        cmd1=str(a.get()) # Get the entered OTP
        cmd='python verify.py '+cmd1 
        os.system(cmd) # call the verify program
        ok='Invalid OTP: '+str((count-1))+' attempts remaining' 
        count=count-1
        f1=open("Status.txt","r")
        bh=f1.read()
        if count>=1 and bh != "success":
            tkinter.messagebox.askretrycancel("Error", ok)
            f1.close()
        elif count == 0 and bh != "success":
            f=open("OTP.txt","w")
            f.write("")
            f.close()
            messagebox.showinfo("Oooo","Your 3 attempts was over. Please regenerate OTP")
            f1.close()
            Window.destroy()
        elif bh == "success":
            f1.close()
            Window.destroy()

start=time.time() # Timer started once the screen is entered
label1=Label(Window,text="Verification Screen",font=("arial",20,"bold"),fg='blue')
label1.place(x=130,y=30)
a=StringVar()
Re=Label(Window,text="Enter Your OTP",font="arial 15 bold").place(x=110,y=94)
w1=Entry(Window,width=20,textvariable=a)
w1.place(x=280,y=100)
Re1=Label(Window,text="Please enter within 2 minutes",font=("arial",10,"bold")).place(x=550,y=50)
ver = Button(Window, text="Verify",relief="raised", bg='orange', font="arial 15 bold",command=verify)
ver.place(x=221,y=150)
Window.mainloop()