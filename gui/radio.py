from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title(" tkinter ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')

#r = IntVar()
#r.set("2")

Modes=[
	("pepperoni","pepperoni"),
	("cheese","cheese"),
	("mushroom","mushroom"),
	("onion","onion"),
]

pizz = StringVar()
pizz.set("pepperoni")

for text,mode in Modes:
	Radiobutton(root,text=text,variable=pizz,value=mode).pack(anchor=W)


def clicked(value):
	mylabel=Label(root,text=value)
	mylabel.pack()


#Radiobutton(root,text="Option1",variable=r,value=1,command = lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option2",variable=r,value=2, command = lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option3",variable=r,value=3, command = lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option4",variable=r,value=4, command = lambda: clicked(r.get())).pack()
#mylabel=Label(root,text=r.get())
#mylabel.pack()


#mylabel=Label(root,text=pizz.get())
#mylabel.pack()

#mybutton = Button(root,text="CLick me",command = lambda: clicked(r.get())).pack()
mybutton = Button(root,text="CLick me",command = lambda: clicked(pizz.get())).pack()

root.mainloop()