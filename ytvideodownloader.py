import tkinter
from tkinter import *
from tkinter import ttk
from pytube import YouTube
import threading


# App frame
app = tkinter.Tk()
app.geometry("500x460")
app.title("Youtube Downloader")
app.resizable(height=False, width=False)
canvas = Canvas(app, width=500, height=460)
canvas.pack()


# UI elements
logo = PhotoImage(file="youtubelogo.png")
logo = logo.subsample(10, 10)
label = ttk.Style()
label.configure("TLabel", foreground="#000000", font=("OCR A Extended", 14))


# We add the elements to the canvas
canvas.create_image(250, 80, image=logo)


# Running the app
app.mainloop()
