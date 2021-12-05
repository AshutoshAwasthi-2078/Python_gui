from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title(" tkinte try ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')
root.geometry("400x600")


conn = sqlite3.connect('address_book.db')   #create and connect to database
c = conn.cursor()                           #create cursor


#create table
'''
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")                                        
'''


def delete():

	conn = sqlite3.connect('address_book.db')   #create and connect to database
	c = conn.cursor()
	c.execute("DELETE from addresses WHERE oid="+de.get()) 
	conn.commit()                               #commit changes
	conn.close()


def submit():

	conn = sqlite3.connect('address_book.db')   #create and connect to database
	c = conn.cursor() 
	c.execute("INSERT INTO addresses VALUES(:f_name, :l_name,:address, :city, :state, :zipcode)",
		{
		'f_name':f_name.get(),
		'l_name':l_name.get(),
		'address':address.get(),
		'city':city.get(),
		'state':state.get(),
		'zipcode':zipcode.get(),
		})
	conn.commit()                               #commit changes
	conn.close()

	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)


def query():
	conn = sqlite3.connect('address_book.db')   #create and connect to database
	c = conn.cursor()

	c.execute("SELECT *,oid FROM addresses")
	records=c.fetchall()
	print_records=''

	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

	query_label=Label(root,text=print_records) 
	query_label.grid(row=12, column=0, columnspan=2)

	conn.commit()                               #commit changes
	conn.close()

def update():
	conn = sqlite3.connect('address_book.db')   #create and connect to database
	c = conn.cursor()

	record_id=de.get()

	c.execute("""UPDATE addresses SET
		first_name =:first,
		last_name = :last,
		address = :address,
		city = :city,
		state =:state,
		zipcode =:zipcode

		WHERE oid =  :oid""",
		{
		'first':f_name_edit.get(),
		'last':l_name_edit.get(),
		'address':address_edit.get(),
		'city':city_edit.get(),
		'state':state_edit.get(),
		'zipcode':zipcode_edit.get(),
		'oid':record_id
		})

	conn.commit()                               #commit changes
	conn.close()
	editor.destroy()



def edit():
	global editor
	editor = Tk()
	editor.title(" tkinte try ")
	editor.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')
	editor.geometry("400x300")


	conn = sqlite3.connect('address_book.db')   #create and connect to database
	c = conn.cursor()

	record_id=de.get()
	c.execute("SELECT * FROM addresses WHERE oid = " +record_id)
	records=c.fetchall()


	global f_name_edit
	global l_name_edit
	global address_edit
	global city_edit
	global state_edit
	global zipcode_edit

	
	#Entry
	f_name_edit=Entry(editor,width=30)
	f_name_edit.grid(row=0,column=1,padx=20,pady=(10,0))
	l_name_edit=Entry(editor,width=30)
	l_name_edit.grid(row=1,column=1,padx=20)
	address_edit=Entry(editor,width=30)
	address_edit.grid(row=2,column=1,padx=20)
	city_edit=Entry(editor,width=30)
	city_edit.grid(row=3,column=1,padx=20)
	state_edit=Entry(editor,width=30)
	state_edit.grid(row=4,column=1,padx=20)
	zipcode_edit=Entry(editor,width=30)
	zipcode_edit.grid(row=5,column=1,padx=20)
	

	#label
	fnamelabel=Label(editor,text = "first Name")
	fnamelabel.grid(row=0,column=0,pady=(10,0))
	lnamelabel=Label(editor,text = "Last Name")
	lnamelabel.grid(row=1,column=0)
	addlabel=Label(editor,text = "address")
	addlabel.grid(row=2,column=0)
	citylabel=Label(editor,text = "city")
	citylabel.grid(row=3,column=0)
	statelabel=Label(editor,text = "State")
	statelabel.grid(row=4,column=0)
	zipcodelabel=Label(editor,text = "Zipcode")
	zipcodelabel.grid(row=5,column=0)

	for record in records:
		f_name_edit.insert(0,record[0])
		l_name_edit.insert(0,record[1])
		address_edit.insert(0,record[2])
		city_edit.insert(0,record[3])
		state_edit.insert(0,record[4])
		zipcode_edit.insert(0,record[5])


	edit_btn=Button(editor,text="Save Record",command=update)
	edit_btn.grid(row=6,column=0,columnspan=2, padx=10, pady=10, ipadx=138)



	


#Entry
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)
de=Entry(root,width=30)
de.grid(row=9,column=1,padx=20,pady=5)


#label
fnamelabel=Label(root,text = "first Name")
fnamelabel.grid(row=0,column=0,pady=(10,0))
lnamelabel=Label(root,text = "Last Name")
lnamelabel.grid(row=1,column=0)
addlabel=Label(root,text = "address")
addlabel.grid(row=2,column=0)
citylabel=Label(root,text = "city")
citylabel.grid(row=3,column=0)
statelabel=Label(root,text = "State")
statelabel.grid(row=4,column=0)
zipcodelabel=Label(root,text = "Zipcode")
zipcodelabel.grid(row=5,column=0)
dellabel=Label(root,text = "Delete ID")
dellabel.grid(row=9,column=0,pady=5)



submitbtn=Button(root,text="Add record",command=submit)
submitbtn.grid(row=6,column=0,columnspan=2, padx=10, pady=10, ipadx=141)


query_btn=Button(root,text="Show Record",command=query)
query_btn.grid(row=7,column=0,columnspan=2, padx=10, pady=10, ipadx=137)

del_btn=Button(root,text="Delete Record",command=delete)
del_btn.grid(row=10,column=0,columnspan=2, padx=10, pady=10, ipadx=135)


edit_btn=Button(root,text="Edit Record",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2, padx=10, pady=10, ipadx=138)



conn.commit()                               #commit changes
conn.close()                                #close connection




root.mainloop()