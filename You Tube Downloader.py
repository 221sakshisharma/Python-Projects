import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from pathlib import Path

window = tk.Tk()
window.title("You Tube Downloader")
window.geometry("700x200")
window.resizable(False, False)

video_title = tk.StringVar()
home_path = Path.home()

# Creating Widgets

fields = {"url_text": ttk.Label(window, text="URL: "),
          "url_input": ttk.Entry(window),
          "video_name": ttk.Label(window, textvariable=video_title)}

for field in fields.values():
    field.pack(fill=tk.X, padx=5, pady=2)


# Creating Functions

def show_title():
    global video_title
    video = YouTube(fields["url_input"].get())
    video_title.set(f"Title: {video.title}")
    fields["video_name"].pack()


def download_mp4():
    path = str(Path.joinpath(home_path, "Videos"))
    video = YouTube(fields["url_input"].get()).streams.get_highest_resolution()
    print(video)
    video.download(path)


def download_mp3():
    path = str(Path.joinpath(home_path, "Music"))
    audio = YouTube(fields["url_input"].get()).streams.get_audio_only()
    print(audio)
    audio.download(path)


buttons = {
    "show_button": ttk.Button(window, text="Show Title", command=lambda: show_title()),
    "download_mp4_button": ttk.Button(window, text="Download Video", command=lambda: download_mp4()),
    "download_mp3_button": ttk.Button(window, text="Download Audio", command=lambda: download_mp3())
}

for button in buttons.values():
    button.pack(anchor=tk.W, padx=5, pady=5)

window.mainloop()
