from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title(" tkinter ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')

frame=LabelFrame(root,text="this is my frame", padx=50,pady=50)
frame.pack(padx=10,pady=5)

b=Button(frame,text="cllick this")
b.pack()




root.mainloop()