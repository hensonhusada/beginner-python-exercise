# Don't know why, but it seems to throw exception with most links
#
from pytube import YouTube

link = input('Youtube link to download (will download 720p): ')
yt = None
while yt is None:
    try:
        yt = YouTube(link)
    except Exception as e:
        print(e)


print("Title: ", yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

choice = input('Download mp4 or mp3? (Y for mp4/else for mp3): ')

if choice.lower() == 'y':
    ys = yt.streams.get_highest_resolution()
    print('Downloading MP4..')
    ys.download('yutub_dlder_files')
    print('Finished downloading!')
else:
    ys = yt.streams.get_by_itag('140')
    print(ys)