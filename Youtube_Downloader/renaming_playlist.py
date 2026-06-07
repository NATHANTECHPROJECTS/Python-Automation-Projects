import yt_dlp
import os

def rename_existing_playlist(playlist_url, folder, logger=None):
    def log(msg):
        if logger:
            logger.info(msg)
        else:
            print(msg)

    log("Fetching playlist order from YouTube...")
    ydl_options = {'quiet': True, 'extract_flat': True, 'noplaylist': False}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(playlist_url, download=False)

    entries = info.get('entries', [])
    if not entries:
        log("No entries found in playlist.")
        return

    folder = os.path.normpath(folder)
    files = set(os.listdir(folder))
    renamed = 0

    for i, entry in enumerate(entries):
        index = entry.get('playlist_index') or (i + 1)
        title = entry.get('title', '')
        if not title:
            continue

        prefix = f"{index:02d} - "

        if any(f.startswith(prefix) for f in files):
            continue

        match = None
        for filename in files:
            name_no_ext = os.path.splitext(filename)[0]
            if name_no_ext.split(' - ')[0].strip().isdigit():
                continue
            if name_no_ext == title:
                match = filename
                break

        if not match:
            for filename in files:
                name_no_ext = os.path.splitext(filename)[0]
                if name_no_ext.split(' - ')[0].strip().isdigit():
                    continue
                if title in name_no_ext:
                    match = filename
                    break

        if match:
            ext = os.path.splitext(match)[1]
            new_name = f"{prefix}{title}{ext}"
            os.rename(os.path.join(folder, match), os.path.join(folder, new_name))
            log(f"Renamed: {match} -> {new_name}")
            files.discard(match)
            files.add(new_name)
            renamed += 1
        else:
            log(f"No match found for: {index:02d} - {title}")

    log(f"\nDone. {renamed} file(s) renamed.")
