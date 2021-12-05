from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title(" tkinte try ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')

def open():
	global myimage
	root.filename = filedialog.askopenfilename(initialdir="/Users/Awasthi/Documents/gui",title="Select a File", filetypes=(("jpg files","*.jpg"),("all files","*.*")))
	label1=Label(root,text=root.filename).pack()
	myimage=ImageTk.PhotoImage(Image.open(root.filename))
	myimglabel=Label(image=myimage).pack()



my_btn=Button(root,text="open file", command=open).pack()
root.mainloop()