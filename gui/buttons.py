from tkinter import *

root = Tk()

def myclick():
	mylabel=Label(root,text="Look! I clicked")
	mylabel.pack()



myButton = Button(root,text="Click Me!",padx=50,command=myclick,fg="#ffffff",bg="black")#state = DISABLED)
myButton.pack()



root.mainloop()