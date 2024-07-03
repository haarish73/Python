from tkinter import *
from PIL import ImageTk, Image

window = Tk()

# Load the background image
background_image = Image.open("doraemon.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas widget and place it at the back of the window
canvas = Canvas(window, width=background_image.width, height=background_image.height)
canvas.pack()

# Place the background image on the Canvas
canvas.create_image(0, 0, anchor=NW, image=background_photo)

# Add widgets and set up your GUI here
frame = Frame(window)
frame.pack()



window.mainloop()
