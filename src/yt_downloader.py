from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views:", yt.views)

print("Getting the highest resolution video for you!")

yd = yt.streams.get_highest_resolution()

print("Downloading your video (this may take a few moments)!")

# change this
path = "/Users/ninge/Videos/YouTube Downloads/"

yd.download(path)

print(f"The YouTube video, {yt.title}, downloaded to {path}!")
