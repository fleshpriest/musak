from yt_dlp import YoutubeDL
from playlistOperations import prepareDownloads
from config import errorLog, ydl_opts

print('Downloading playlist(s) info')
urlList = prepareDownloads()

print('\nDownloading', len(urlList), 'songs')
downloadErrors = []

for i in range(len(urlList)):
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(urlList[i], download=False)
        print(i+1, 'of', len(urlList), ':', info['title'], '-', info['uploader'])
        errorCode = ydl.download(urlList[i])
        if errorCode:
            downloadErrors.append(f'{info['title']} {info['uploader']}')

print('\nFinished downloads')

if downloadErrors:
    from os.path import realpath

    with open(errorLog, 'w') as f:
        for line in downloadErrors:
            f.write(f'{line}\n')

    print(len(downloadErrors), 'files had errors, please check logs')
    print(realpath(errorLog))

