import sys
from tkinter import messagebox
from tkinter import *
import time

b=sys.argv[1]
f1=open("otp.txt","r")
b1=f1.read()
f1.close()
#print(b,b1)
if b==b1:
 f = open("Status.txt", "w")
 f.write("Success!")
 f.close()
 Window = Tk()
 Window.geometry("500x300")
 Window.resizable(0,0)
 Window.title("Success")
 messagebox.showinfo("Congratulations","Your OTP was verified successfully!")
 Window.destroy()
 Window.mainloop()
else:
 f = open("Status.txt", "w")
 f.write("Failure!")
 f.close()