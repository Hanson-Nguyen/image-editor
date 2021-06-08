import os
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog, Text, Button, PhotoImage, Canvas
import tkinter.filedialog
import tkFileDialog

gui = tk.Tk()
gui.resizable(True, True)
gui.geometry("1600x900")
gui.configure(background = 'black')
gui.title("Image Editor")

frame = tk.Frame(gui, bg = "white")
frame.place(relwidth = 1, relheight = 0.9, relx = 0, rely = 0)
frame.configure(background = 'teal')

canvas = Canvas(gui, width = 750, height = 750, highlightthickness = 0, bg = 'teal')
canvas.grid()

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

content = 'apple'
file_path = 'banana'

def selectImage(self):
    myfile = filedialog.askopenfilename()

buttonOpenImage = Button(gui, text = "Open Image", command = lambda:openImage(gui))
buttonOpenImage.grid(row = 5, column = 3)

buttonChooseImage = Button(gui, text = "Select Image", command = lambda:selectImage(gui))
buttonChooseImage.grid(row = 6, column = 3)

gui.mainloop()
