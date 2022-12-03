import click
from service import download_yt_video, create_gif


@click.command()
@click.argument('url')
@click.option('--from', 'start_time')
@click.option('--to', 'end_time')
@click.option('-o', 'output')
def download_gif(url, start_time, end_time, output):
    download_yt_video(url, start_time, end_time)
    create_gif(output)
    

if __name__ == '__main__':
    download_gif()