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
url = ttk.Label(app, text="Add your Video URL here:", style="TLabel")
url_entry = ttk.Entry(app, width=70, style="TEntry")
resolution = Label(app, text="Resolution:", font="Roboto")
video_res = ttk.Combobox(app, width=10)

# Styles
label = ttk.Style()
label.configure("TLabel", foreground="#000000", font=("Roboto", 14))
entry = ttk.Style()
entry.configure("TEntry", font=("Arial", 15))
button = ttk.Style()
button.configure("TButton", foreground="#000000", font="Roboto")


# We add the elements to the canvas
canvas.create_image(250, 80, image=logo)
canvas.create_window(250, 175, window=url)
canvas.create_window(250, 200, window=url_entry)
canvas.create_window(75, 230, window=resolution)
canvas.create_window(77, 255, window=video_res)


# Running the app
app.mainloop()
