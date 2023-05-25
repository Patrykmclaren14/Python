
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import requests
import json


root = Tk()
root.title('Codemy.com - Learn To Code!')


def zipLookup():

    try:
        api_requests = requests.get(
            'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() + '&distance=20&API_KEY=9E8FE620-A471-4CFB-9FD9-0B24A3641E98')
        api = json.loads(api_requests.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weatherColor = "#0C0"
        elif category == "Moderate":
            weatherColor = "FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weatherColor = "ff9900"
        elif category == "Unhealthy":
            weatherColor = "FF0000"
        elif category == "Very Unhealthy":
            weatherColor = "990000"
        elif category == "Hazardous":
            weatherColor = "#660000"

        root.configure(background=weatherColor)

        myLabel = Label(root, text=city + ' Air Quality: ' +
                        str(quality) + ' Status: ' + category, font=('Helvetica', 20), background=weatherColor)
        myLabel.pack()
    except Exception as e:
        api = "Error"


zip = Entry(root)
zip.pack()

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.pack()

root.mainloop()
