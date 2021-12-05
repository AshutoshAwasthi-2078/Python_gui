from tkinter import *

root = Tk()

mylabel1 = Label(root,text = "Hello World").grid(row=0,column=0)
mylabel2 = Label(root,text = "My name is ashutosh").grid(row=0,column=1)

#mylabel1.grid(row=0,column=0)
#mylabel2.grid(row=1,column=0)

root.mainloop()