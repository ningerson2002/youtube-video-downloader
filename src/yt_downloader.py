from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

print("Downloading...")

# change this value to the path you wish to download to
path = "/Users/ninge/Videos/YouTube Downloads/"

yd.download(path)

print(f"{yt.title} downloaded to {path}!")
