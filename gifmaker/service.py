import ffmpeg
from pytube import StreamQuery, YouTube
from moviepy.editor import VideoFileClip


def get_url(url: str) -> str:
    yt_video = YouTube(url)
    mp4_streams: StreamQuery = yt_video.streams\
        .filter(progressive=True, file_extension='mp4')
    
    url =  None
    for s in mp4_streams:
        if s.resolution == '360p':
            print('Will download video with 360p resoution')
            return s.url

    print('Will download video with best possible resolution')
    return mp4_streams.order_by('resolution').desc().first().url


def download_yt_video(url: str, start_time:str, end_time:str) -> str:
    url_to_download = get_url(url)
    
    ffmpeg.input(url_to_download, ss=start_time, to=end_time).output("demo.mp4",
     vcodec="copy").overwrite_output().run()

def create_gif(output: str):
    videoClip = VideoFileClip("demo.mp4")

    videoClip.write_gif(output, fps=10)
