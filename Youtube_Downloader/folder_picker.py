import tkinter as tk # GUI for oopening file explorer to select download path
from tkinter import filedialog # Create a simple GUI to select the download path

# Pick the folder to where the video will be downloaded
def pick_folder():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # To ensure the diaog appears on to of all the others
    folder = filedialog.askdirectory(title = "Choose the download folder")
    root.destroy()
    return folder