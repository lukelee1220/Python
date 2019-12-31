import sys, tkinter

def myPrint():
    print("Hello World")
tkinter.LabelFrame(text="Test").pack()
tkinter.Label(text="Welcome").pack()
tkinter.Button(text="Exit",command=sys.exit).pack()
tkinter.Button(text="Open",command=myPrint).pack()
tkinter.mainloop()
