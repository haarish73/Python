from tkinter import *


import mysql.connector

from PIL import ImageTk
window = Tk()
frame = Frame(window)
frame.place(x=700,y=100)
usernameLabel = Label(frame,text="username")
usernameLabel.grid(row=0,column=0)
frame.pack()
window.mainloop()
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123"
)
mycur=conn.cursor()
if(mycur) :
    print("Success")
else :
    print("Problem in database")

