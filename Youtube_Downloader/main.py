from folder_picker import pick_folder
from download_video import download_video
from renaming_playlist import rename_existing_playlist

if __name__ == "__main__":
    mode = input("1. Download Video\n2. Download Audio\n3. Rename existing playlist files in order\nEnter your choice (1, 2, or 3): ").strip()
    if mode not in ("1", "2", "3"):
        print("Invalid Choice. Exiting")
        exit()

    if mode == "3":
        playlist_url = input("Enter the Playlist URL: ").strip()
        folder = pick_folder()
        if not folder:
            print("No folder selected. Exiting.")
            exit()
        rename_existing_playlist(playlist_url, folder)
    else:
        video_url = input("Enter the Youtube Video URL: ").strip()
        download_path = pick_folder()
        if not download_path:
            print("No folder Selected. Exiting")
            exit()
        download_video(video_url, download_path, audio_only=(mode == "2"))