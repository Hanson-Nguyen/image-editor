import tkinter as tk
from tkinter import filedialog, Text
import os

gui = tk.Tk()
gui.resizable(True, True)
gui.geometry("1280x720")
gui.configure(background = 'black')
gui.title("Image Editor")

#Aspect Ratio of 16:9

frame = tk.Frame(gui, bg = "white")
frame.place(relwidth = 1, relheight = 0.8, relx = 0, rely = 0)
frame.configure(background = 'teal')


gui.mainloop()
