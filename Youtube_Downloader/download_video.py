import yt_dlp

def download_video(url, download_path, audio_only=False):
    # Configure Options

    if audio_only:
        # For audio Only
        ydl_options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{download_path}/%(playlist_index)s - %(title)s.%(ext)s',
            'noplaylist' : False,
            'nooverwrites': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', # To Extract audio as mp3 
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        # For video and audio
        ydl_options = {
        'format' : 'bestvideo+bestaudio/best', 
        'outtmpl' : download_path + r'\%(playlist_index)s - %(title)s.%(ext)s',
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
