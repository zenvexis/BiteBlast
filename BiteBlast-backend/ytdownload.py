from pytubefix import YouTube
from pytubefix.cli import on_progress


url1 = "https://www.youtube.com/watch?v=qjJpg81UKqY"
url2 = "https://www.youtube.com/watch?v=Xf44xiH3_Ls"

yt = YouTube(url2, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()
