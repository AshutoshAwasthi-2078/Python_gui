from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title(" tkinter ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')


def popup():
	#messagebox.showinfo("This is my popup","Hello World")
	#messagebox.showwarning("This is my popup","Hello World")
	#messagebox.showerror("This is my popup","Hello World")
	#messagebox.askquestion("This is my popup","Hello World")
	#messagebox.askokcancel("This is my popup","Hello World")
	response=messagebox.askyesno("This is my popup","Hello World")
	label1=Label(root,text=response).pack()

	#if response==1:
	#	label1=Label(root,text="You clicked Yes!").pack()
	#else:
	#	label1=Label(root,text="You clicked no!").pack()


Button(root,text="Popup", command=popup).pack()




root.mainloop()