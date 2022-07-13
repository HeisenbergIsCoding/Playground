import pytube


def get_tube_video():
    # youtube link
    tube_link = 'https://www.youtube.com/watch?v=to-qf94qzII'
    yt = pytube.YouTube(tube_link)
    mp4_file = yt.streams.filter(file_extension='mp4', res='720p')
    mp4_file.first().download()


if __name__ == '__main__':
    get_tube_video()
