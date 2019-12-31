import tkinter
import time

tk=tkinter.Tk()
tk.title("Timer Demo")

pauseFlag = False

def set_pauseFlag(flag):
    global pauseFlag
    pauseFlag = flag


def show_label(label):
    global pauseFlag
    str1 = time.asctime(time.localtime())
    label.config( text=str1, font='times 100',bg="blue" )
    if pauseFlag == False:
        tk.after(500,show_label,label)

def start(label):
    set_pauseFlag(False)
    show_label(label)

label1 = tkinter.Label(tk, text="Hello World",justify='center', font='times 50', bg="green" )
label1.pack()

button1 = tkinter.Button(text="Start", command = lambda: start(label1))
button1.pack()
button2 = tkinter.Button(text="Stop", command = tk.destroy, bg="red")
button2.pack()
button3 = tkinter.Button(text="Pause", command = lambda: set_pauseFlag(True), bg="green")
button3.pack()

tk.mainloop()
