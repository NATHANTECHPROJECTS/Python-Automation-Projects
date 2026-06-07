import yt_dlp
import os

def download_video(url, download_path, audio_only=False, logger=None):
    base = {
        'outtmpl': os.path.join(download_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'noplaylist': False,
        'nooverwrites': True,
    }

    if audio_only:
        ydl_options = {
            **base,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_options = {
            **base,
            'format': 'bestvideo+bestaudio/best',
        }

    if logger:
        ydl_options['logger'] = logger

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])
