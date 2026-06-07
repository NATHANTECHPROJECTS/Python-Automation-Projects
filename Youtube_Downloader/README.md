# YouTube Downloader

A desktop GUI application for downloading YouTube videos, audio, and renaming playlist files — built with Python, Tkinter, and yt-dlp.

---

## Features

- **Download Video** — Downloads the best available video + audio quality
- **Download Audio (MP3)** — Extracts audio and converts it to MP3 at 192kbps
- **Rename Playlist Files** — Fetches the playlist order from YouTube and renames already-downloaded local files to match the correct `index - title` format
- **Playlist support** — All download modes work with both single videos and full playlists
- **Background threading** — Downloads run in a background thread so the UI stays responsive
- **Live log output** — Progress and status messages are streamed directly into the app window

---

## Screenshots

> _Add screenshots here once available._

---

## Requirements

- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/) (required for MP3 conversion and merging video+audio streams)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/youtube-downloader.git
   cd youtube-downloader
   ```

2. **Install Python dependencies**

   ```bash
   pip install yt-dlp
   ```

3. **Install FFmpeg**

   - **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your system PATH
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt install ffmpeg`

---

## Usage

Run the application:

```bash
python main.py
```

### Download Video

1. Paste a YouTube video or playlist URL into the **URL** field
2. Select **Download Video**
3. Click **Start** and choose a destination folder
4. The best available quality video will be saved to that folder

### Download Audio (MP3)

1. Paste a YouTube video or playlist URL into the **URL** field
2. Select **Download Audio (MP3)**
3. Click **Start** and choose a destination folder
4. Audio is extracted and saved as an MP3 at 192kbps

### Rename Existing Playlist Files

Use this if you downloaded a playlist earlier but the files are missing their playlist index numbers (e.g., `01 - `, `02 - ` prefixes).

1. Paste the **playlist URL** into the URL field
2. Select **Rename existing playlist files in order**
3. Click **Start** and select the folder containing the already-downloaded files
4. The app fetches the playlist order from YouTube and renames files to match

> Files that already have a numeric prefix are skipped. Matching is attempted by exact title first, then by substring.

---

## Project Structure

```
Youtube_Downloader/
├── main.py                # Entry point — launches the GUI
├── GUI.py                 # Tkinter application window and logger
├── download_video.py      # yt-dlp download logic (video and audio)
├── renaming_playlist.py   # Playlist order fetching and file renaming
└── folder_picker.py       # Native folder selection dialog
```

---

## File Naming

Downloaded files follow this naming convention:

```
<playlist_index> - <title>.<ext>
```

Example:
```
01 - My Favourite Song.mp3
02 - Another Great Track.mp3
```

Single video downloads without a playlist index will just use the title.

---

## Known Limitations

- FFmpeg must be installed and available on PATH for MP3 downloads and for merging separate video/audio streams
- The rename feature relies on YouTube's playlist metadata — if a video has been removed from the playlist, it will report "No match found" for that entry
- Very long titles may cause issues on filesystems with short path limits (e.g., Windows MAX_PATH)

---

## License

This project is for personal use. Check [yt-dlp's FAQ](https://github.com/yt-dlp/yt-dlp/wiki/FAQ) for guidance on terms of service compliance.
