from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Digite a URL do vídeo: ")
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download()

print('-' * 20)
print('Download completo')
print('-' * 20)
