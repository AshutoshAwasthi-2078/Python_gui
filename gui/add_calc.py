from tkinter import *

root = Tk()
label1 =Label(root,text="Addition")


e1 = Entry(root,width=50)
e1.pack()
e1.insert(0,"Enter first number")


e2 = Entry(root,width=50)
e2.pack()
e2.insert(0,"Enter second number")

def add():
	res = int(e1.get()) + int(e2.get())
	lb = Label(root,text = res)
	lb.pack()

mybutton = Button(root,text ="Submit",command = add)
mybutton.pack()

root.mainloop()