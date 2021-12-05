from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title(" tkinte try ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')
root.geometry("400x400")


options=["Monday","Tuesday","Wednesday","Thursday"]

var = StringVar()
#var.set("Monday")
var.set(options[0])

#drop=OptionMenu(root,var,"Monday","Tuesday","Wednesday","Thursday")

drop=OptionMenu(root,var,*options)
drop.pack()


root.mainloop()