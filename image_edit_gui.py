import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog, Text, Button, PhotoImage, Canvas
import os

gui = tk.Tk()
gui.resizable(True, True)
gui.geometry("1280x720")
gui.configure(background = 'black')
gui.title("Image Editor")

frame = tk.Frame(gui, bg = "white")
frame.place(relwidth = 1, relheight = 0.9, relx = 0, rely = 0)
frame.configure(background = 'teal')

canvas = Canvas(gui, width = 600, height = 600, highlightthickness = 0, bg = 'teal')
canvas.pack()

def openImage(self):
    img = Image.open("test1.gif")

    #checking size of image to resize image and keep ratio
    width, height = img.size

    wratio = 1
    hratio = 1

    if (height > width):
        wratio = width/height 
    if (width > height):
        hratio = height/width

    img2 = img.resize((round(wratio * 750), round(hratio * 750)), Image.ANTIALIAS)
    resized = ImageTk.PhotoImage(img2)
    self.img = resized
    canvas.create_image(0, 0, anchor = "nw", image = resized) 

buttonOpenImage = Button(gui, text = "Open Image", command = lambda:openImage(gui))
buttonOpenImage.pack(padx = 50, pady = 50)

gui.mainloop()
