from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title(" tkinte try ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')

def open():
	global my_img1
	top = Toplevel()
	top.title(" New ")
	top.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')
	my_img1 = ImageTk.PhotoImage(Image.open("para1.jpg"))
	label1=Label(top,image=my_img1).pack()
	btn2 = Button(top,text="Close window",command=top.destroy).pack()

btn = Button(root,text="Open new window",command=open).pack()







root.mainloop()