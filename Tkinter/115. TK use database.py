from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('first window')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)  # loading icons
root.geometry('400x400')

# Create a database or connect to one
conn = sqlite3.connect('addressBook.db')

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        zipcode integer
)


""")


# Commit Changes
conn.commit()

# Close connection
conn.close()

mainloop()
