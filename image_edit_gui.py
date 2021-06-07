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
frame.place(relwidth = 1, relheight = 0.8, relx = 0, rely = 0)
frame.configure(background = 'teal')

canvas = Canvas(gui, width = 500, height = 500)
canvas.pack()

def openImage(self):
    img = Image.open("cat.jpg")
    img2 = img.resize((500,500), Image.ANTIALIAS)
    resized = ImageTk.PhotoImage(img2)
    self.img = resized
    canvas.create_image(50, 50, anchor = "nw", image = resized) 

buttonOpenImage = Button(gui, text = "Open Image", command = lambda:openImage(gui))
buttonOpenImage.pack()

gui.mainloop()
