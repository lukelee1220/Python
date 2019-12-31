from tkinter import *
import time
tk=Tk()

def my_UTC(label):
    t=time.strftime('UTC %I:%M:%S',time.gmtime())
    if t!='':
        label.config(text=t,font='times 25')
    tk.after(100,my_UTC,label)

def my_localtime(label):
    t=time.strftime('LOCAL %I:%M:%S',time.localtime())
    if t!='':
        label.config(text=t,font='times 25')
    tk.after(100,my_localtime,label)

def my_mktime(label):
    # Local time
    t1=time.mktime(time.localtime())

    # UTC
    t2=time.mktime(time.gmtime()) 
    
    str1 = "%d"%t1 + " %d"%t2
    label.config(text=str1,font='times 25')
    tk.after(100,my_mktime,label)

def my_all(label):
    # Local time
    #t1 = time.mktime(time.localtime())
    str1 = time.asctime(time.localtime())
    label.config(text=str1,font='times 25')
    tk.after(100,my_all,label)


label1=Label(tk,justify='center')
label1.pack()
my_UTC(label1)

label2=Label(tk,justify='center')
label2.pack()
my_localtime(label2)

label3=Label(tk,justify='center')
label3.pack()
my_mktime(label3)

label4=Label(tk,justify='center')
label4.pack()
my_all(label4)

tk.mainloop()

