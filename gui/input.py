from tkinter import *

root = Tk()


e = Entry(root,width=50,borderwidth=10)
e.pack()
e.insert(0,"Enter Your Name")

def myclick():
	hello = " Hello "+e.get()
	mylabel=Label(root,text=hello)
	mylabel.pack()



myButton = Button(root,text="Enter your name",padx=50,command=myclick,fg="#ffffff",bg="black")#state = DISABLED)
myButton.pack()



root.mainloop()