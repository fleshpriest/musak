from os.path import normpath, exists
from os import mkdir, remove
from pathlib import Path
import env

# location where data files are stored
dataDir = 'data'
if not exists(dataDir):
    mkdir(dataDir)

fileAllEntries = normpath(f'{dataDir}/allEntries')
if exists(fileAllEntries):
    remove(fileAllEntries) # Start with a blank slate to avoid having to clean up the file with subsequent runs

filePrevDownloads = normpath(f'{dataDir}/previousDownloads')
if not exists(filePrevDownloads):
    Path(filePrevDownloads).touch()

errorLog = normpath(f'{dataDir}/errorLog')

# Check for deno
if not exists('/usr/bin/deno'):
    print('ERROR: dir /usr/bin/deno not found. Please install deno')
    quit(1)


class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


ydl_opts = {
    'cookiesfrombrowser': (env.browser, None, None, None),
    'download_archive': filePrevDownloads,
    'extract_flat': 'discard_in_playlist',
    'final_ext': env.codec,
    'format': 'bestaudio/best',
    'fragment_retries': 10,
    'ignoreerrors': 'only_download',
    'js_runtimes': {'deno': {'path': '/usr/bin/deno'}},
    'logger': MyLogger(),
    'outtmpl': {'default': '%(title)s - %(uploader)s', 'pl_thumbnail': ''},
    'paths': {'home': env.outputDir},
    'postprocessors': [{'key': 'FFmpegExtractAudio',
                        'nopostoverwrites': False,
                        'preferredcodec': env.codec,
                        'preferredquality': '0'},
                       {'add_chapters': True,
                        'add_infojson': 'if_exists',
                        'add_metadata': True,
                        'key': 'FFmpegMetadata'},
                       {'already_have_thumbnail': False, 'key': 'EmbedThumbnail'},
                       {'key': 'FFmpegConcat',
                        'only_multi_video': True,
                        'when': 'playlist'}],
    'quiet': True,
    'remote_components': ['ejs:github'],
    'restrictfilenames': True,
    'retries': 10,
    'sleep_interval_requests': 0.0,
    'warn_when_outdated': True,
    'writethumbnail': True }
