from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_audio(url, name="", output_dir="temp/"):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    if name == "":
        name = yt.title

    ys = yt.streams.get_audio_only()
    ys.download(output_path=output_dir,filename=f"{name}.m4a")
    return yt.title