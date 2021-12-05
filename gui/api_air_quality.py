from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title(" tkinte try ")
root.iconbitmap('C:/Users/Awasthi/Documents/gui/para.jpg')
root.geometry("600x100")

def ziplookup():
	zip.get()
	#ziplabel = Label(root, text =zip.get())
	#ziplabel.grid(row=1,column=0,columnspan=2)

	try:
		api_request = requests.get("Url for api")   # url + zip.get() +url left
		api=json.loads(api_request.content)

		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category == "Good":
			weather_color = "#0C0"
		elif category == "Moderate":
			weather_color == "#FFFF00"
		elif category == "Unhealthy for sensitive groups":
			weather_color == "#ff9900"
		elif category == "Unhealthy":
			weather_color == "#FF0000"
		elif category == "Very Unhealthy":
			weather_color == "#990066"
		elif category == "Hazardous":
			weather_color == "#660000"

		root.configure(background=weather_color)
		my_label = Label(root,text=city + " Air quality" + str(quality) + category,font=("Helvetica",20),background=weather_color)
		my_label.grid(row=1,column=0,columnspan=2)

	except Exception as e:
		api = "Error...."

zip=Entry(root)
zip.grid(row=0,column=0, stick=W+E+N+S)

zipbtn=Button(root,text="Lookup Zipcode",command=ziplookup)
zipbtn.grid(row=0,column=1, stick=W+E+N+S)

root.mainloop()