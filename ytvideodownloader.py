from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror, askokcancel
import threading
import threading


# App frame
app = Tk()
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
search_res = ttk.Button(app, width=10, text="Search")
progress_bar_label = Label(app, text="")
download_button = ttk.Button(app, text="Download Video", style="TButton")

# Styles
label = ttk.Style()
label.configure("TLabel", foreground="#000000", font=("Roboto", 14))
entry = ttk.Style()
entry.configure("TEntry", font=("Arial", 15))
button = ttk.Style()
button.configure("TButton", foreground="#000000", font="Roboto")
progress_bar = ttk.Progressbar(app, orient=HORIZONTAL, length=450, mode="determinate")


# We add the elements to the canvas
canvas.create_image(250, 80, image=logo)
canvas.create_window(250, 175, window=url)
canvas.create_window(250, 200, window=url_entry)
canvas.create_window(75, 230, window=resolution)
canvas.create_window(77, 255, window=video_res)
canvas.create_window(175, 255, window=search_res)
canvas.create_window(250, 290, window=progress_bar_label)
canvas.create_window(250, 350, window=progress_bar)
canvas.create_window(250, 400, window=download_button)


# App functionality
def searchResolutionVideo():
    link = url_entry.get()
    if link == "":
        showerror(title="Error", message="The link section cannot be empty!")
    else:
        try:
            video = YouTube(link)
            resolutions = []
            # We loop throu the video streams
            for i in video.streams.filter(file_extension="mp4"):
                resolutions.append(i.resolution)
            # We add the resolutions into the combobox
            video_res["values"] = resolutions
            showinfo(
                title="Search complete",
                message="Look for your desired resolution inside the box",
            )
        except:
            showerror(
                title="Error",
                message="An error occurred while searching for the video resolutions",
            )


# Function to run the search function as a thread
def searchThread():
    thread1 = threading.Thread(target=searchResolutionVideo)
    thread1.start()


# Running the app
app.mainloop()
