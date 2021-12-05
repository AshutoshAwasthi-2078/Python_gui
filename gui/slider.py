from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title(" tkinte try ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')
root.geometry("400x400")

vertical=Scale(root,from_=0,to=200)
vertical.pack()

def slide():
	mylabel=Label(root,text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal=Scale(root,from_=0,to=200, orient=HORIZONTAL)
horizontal.pack()  


mylabel=Label(root,text=horizontal.get()).pack()

mybtn=Button(root,text="click me!",command=slide).pack

root.mainloop()