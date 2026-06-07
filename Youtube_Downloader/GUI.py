import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading # For background downloading

from download_video import download_video
from renaming_playlist import rename_existing_playlist
from folder_picker import pick_folder


class GUILogger: # Captures messages (debug, info, warning, error) and displays them in the app's output box instead of the terminal
    def __init__(self, app):
        self.app = app

    def debug(self, msg):
        if '[download]' in msg:
            self.app.log(msg)

    def info(self, msg):
        self.app.log(msg)

    def warning(self, msg):
        self.app.log(f"Warning: {msg}")

    def error(self, msg):
        self.app.log(f"Error: {msg}")


class App(tk.Tk):
    def __init__(self):  # Initialize the 
        super().__init__()
        self.title("YouTube Downloader")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        pad = {'padx': 15, 'pady': 6}

        tk.Label(self, text="YouTube Downloader", font=("Helvetica", 16, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(15, 5)
        )

        tk.Label(self, text="URL:").grid(row=1, column=0, sticky='e', **pad)
        self.url_var = tk.StringVar()
        tk.Entry(self, textvariable=self.url_var, width=55).grid(row=1, column=1, sticky='w', **pad)

        tk.Label(self, text="Mode:").grid(row=2, column=0, sticky='ne', **pad)
        self.mode_var = tk.StringVar(value="1")
        frame = tk.Frame(self)
        frame.grid(row=2, column=1, sticky='w', **pad)
        tk.Radiobutton(frame, text="Download Video", variable=self.mode_var, value="1").pack(anchor='w')
        tk.Radiobutton(frame, text="Download Audio (MP3)", variable=self.mode_var, value="2").pack(anchor='w')
        tk.Radiobutton(frame, text="Rename existing playlist files in order", variable=self.mode_var, value="3").pack(anchor='w')

        self.start_btn = tk.Button(self, text="Start", width=20, command=self._start)
        self.start_btn.grid(row=3, column=0, columnspan=2, pady=10)

        self.output = scrolledtext.ScrolledText(self, width=72, height=16, state='disabled')
        self.output.grid(row=4, column=0, columnspan=2, padx=15, pady=(0, 15))

    def log(self, msg):
        self.after(0, self._write, msg)

    def _write(self, msg):
        self.output.configure(state='normal')
        self.output.insert(tk.END, msg + '\n')
        self.output.see(tk.END)
        self.output.configure(state='disabled')

    def _start(self):
        url = self.url_var.get().strip()
        if not url:
            self.log("Please enter a URL.")
            return

        folder = pick_folder()
        if not folder:
            self.log("No folder selected.")
            return

        mode = self.mode_var.get()
        self.start_btn.configure(state='disabled')
        logger = GUILogger(self)

        def run():
            try:
                if mode == "3":
                    rename_existing_playlist(url, folder, logger=logger)
                else:
                    self.log("Starting download...")
                    download_video(url, folder, audio_only=(mode == "2"), logger=logger)
                    self.log("Download completed successfully!")
            except Exception as e:
                self.log(f"Error: {e}")
            finally:
                self.after(0, self.start_btn.configure, {'state': 'normal'})

        threading.Thread(target=run, daemon=True).start()

