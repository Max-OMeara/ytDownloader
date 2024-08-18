from distutils.errors import DistutilsTemplateError
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete!')
#Image logo (THIS SHIT DONT WORK)
#logo_img = PhotoImage(file='yt.png')

#logo_img = logo_img.subsample(2, 2)

#canvas.create_image(250, 80, image=logo_img)

link_field = Entry(screen, width=50)
link_label = Label(screen, text= "Enter Download Link: ", font=('Arial', 15))

path_label = Label(screen, text="Select Path for Download", font=('Arial', 15))
select_btn = Button(screen, text="Select", command=select_path)

canvas.create_window(250, 250, window=path_label)
canvas.create_window(250, 280, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

download_btn = Button(screen, text="Download File", font=('Arial', 15), command=download_file)

canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
#This creates the application
