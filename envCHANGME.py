from os.path import normpath

# List of all playlists you wish to grab music from
myPlaylists = (
    "https://www.youtube.com/playlist?list=PLfP6i5T0-DkK-1uhfhicxlQ2FJwbuA7uU",
    "https://www.youtube.com/playlist?list=PL7pkSK1xbGD7opCI4ltKWdkH2ohjSTBzk",
)

# Directory where files will be saved to
outputDir = normpath("/path/to/dir")

# Browser where YouTube login cookies are stored, used to get around age restricted videos
# Options: brave, chrome, chromium, edge, firefox, opera, safari, vivaldi, whale
browser = 'firefox'

# Preferred audio file format
# Options: aac, alac, flac, m4a, mp3, opus, vorbis, wav
codec = 'flac'
