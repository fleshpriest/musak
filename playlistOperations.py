from env import myPlaylists
from config import *
from yt_dlp import YoutubeDL

def prepareDownloads ():
    pl_opts = {'extract_flat': 'in_playlist',
               'ignoreerrors': True,
               'noprogress': True,
               'print_to_file': {'video': [('id', fileAllEntries)]},
               'quiet': True,
               'simulate': True
               }

    # Download playlist info from YouTube
    for playlist in myPlaylists:
        with YoutubeDL(pl_opts) as ydl:
            infoPL = ydl.extract_info(playlist, download=False)
            print(infoPL['title'], infoPL['uploader'], "-", infoPL['playlist_count'], "videos")

    # Load allEntries file into python
    seenUrls = []
    with open(fileAllEntries, 'r') as file:
        for line in file:
            seenUrls.append(line)

    # Sanitize seenUrl strings
    for i in range(len(seenUrls)):
        seenUrls[i] = seenUrls[i].split('\n')[0]

    # Load previous downloads into python
    downloadedUrls = []
    with open(filePrevDownloads, 'r') as file:
        for line in file:
            downloadedUrls.append(line)

    # Sanitize downloadedUrls strings
    for i in range(len(downloadedUrls)):
        downloadedUrls[i] = downloadedUrls[i].split(' ', 2)[1].split('\n')[0]

    # Removes previously downloaded & duplicate URLs from final list
    newUrls = list(set(seenUrls) - set(downloadedUrls))

    # Sanitize final list
    for url in newUrls:
        url = url.replace('\n', '')

    return newUrls
