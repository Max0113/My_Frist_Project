import yt_dlp

url = "https://www.youtube.com/watch?v=N1VUvq0Tnrg"

ydl_opts = {'format': '399'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
