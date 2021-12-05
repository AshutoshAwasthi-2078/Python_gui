from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title(" tkinte try ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')
root.geometry("400x400")

def show():
	mylabel=Label(root,text=var.get()).pack()

#var = IntVar()
var = StringVar()

c=Checkbutton(root,text="check this",variable=var,onvalue="checked",offvalue="not checked")
c.deselect()
c.pack()

mybtn=Button(root,text="show",command=show).pack()

root.mainloop()