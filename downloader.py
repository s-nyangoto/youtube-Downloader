# importing the module
from pytube import YouTube
import os

# where to save
SAVE_PATH = "/Users/Mikekebaso/Desktop" # to_do

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=4OkPzXBBjPs"

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")

# filters out all the files with "mp4" extension
mp4files = list(yt.streams.filter(file_extension='mp4'))

if not mp4files:
    print("No MP4 files available for download.")
else:
    # to set the name of the file
    yt.streams.get_by_itag(mp4files[-1].itag).download(output_path=SAVE_PATH)
    print('Task Completed!')
