import yt_dlp # Youtube library
import tkinter as tk # GUI for oopening file explorer to select download path
from tkinter import filedialog # Create a simple GUI to select the download path

# Pick the folder to where the video will be downloaded
def pick_folder():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder = filedialog.askdirectory(title = "Choose the download folder")
    root.destroy()
    return folder


# Function to download a YouTube video - Takes in the video URL as the parameter
def download_video(url, download_path, audio_only=False):
    # Configure Options
    if audio_only:
        ydl_options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'noplaylist' : False,
            'nooverwrites': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_options = {
        'format' : 'bestvideo+bestaudio/best',
        'outtmpl' : download_path + r'\%(title)s.%(ext)s',
        'noplaylist' : False,
        'nooverwrites': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            print("Downloading video...")
            ydl.download([url])
            print("\nDownload Completed Successfully!")
    except Exception as e:
        print(f"An error {e} occurred while downloading the video")

if __name__ == "__main__":
    video_url = input("Enter the Youtube Video URL: ")

    mode = input("Download 1. Video\n2. Audio\nEnter your choice (1 or 2): ")
    if mode not in ("1", "2"):
        print("Invalid Choice. Exiting")
        exit()

    download_path = pick_folder()
    if not download_path:
        print("No folder Selected. Exiting")
        exit()

    download_video(video_url, download_path, audio_only = (mode == "2"))
