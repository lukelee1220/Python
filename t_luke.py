import tkinter 
import time
k=tkinter
i=time

tk=tkinter.Tk()

def show_label(label):
    str1=i.asctime(i.localtime())
    label.config( text=str1, font='times 25',bg="red" )
    tk.after(500,show_label,label)


label1=k.Label(tk, text="Hello World",bg="blue", font="time 32")
label1.pack()

button1=k.Button(tk, text="start",bg="blue", command=lambda:show_label(label1))
button1.pack()

button1=k.Button(tk, text="stop",bg="blue", command=tk.destroy)
button1.pack()

button1=k.Button(tk, text="post",bg="green", command=lambda:show_label(label1))
button1.pack()


tk.mainloop()



