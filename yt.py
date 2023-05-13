# importing the module
from pytube import YouTube
video_list = open("sample.txt","r")
for i in video_list:
    yt = YouTube(i)
    try :
        dw=yt.streams.get_highest_resolution()
        dw.download()
    except:
        print("Download failed for",i)

