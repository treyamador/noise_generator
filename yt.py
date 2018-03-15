from pytube import YouTube
import moviepy.editor as mp
import argparse
import imageio
import eyed3
import sys
import re


def init():
    imageio.plugins.ffmpeg.download()


def command_line():
    args = sys.argv[1:]
    if len(args) == 0:
        return print('Enter a url.')
    elif len(args) == 1:
        return args[0]
    else:
        return args[0]


def download(url):
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4')\
        .order_by('resolution').desc().first().download()
    try:
        print(yt.title+' downloaded.\nConverting...')
    except UnicodeError:
        print('Video downloaded.\nConverting...')
    return yt


def convert_mp4_to_mp3(fn):
    clip = mp.VideoFileClip(fn+'.mp4')
    clip.audio.write_audiofile(fn+'.mp3')
    print('Conversion completed.\nUpdating tags...')


def update_tag(fn):
    tags = [x.strip() for x in re.split('-|\[|\]|\(|\)',fn)]
    audiofile = eyed3.load(fn+'.mp3')
    try:
        audiofile.tag.artist = u''+tags[0]
        audiofile.tag.album_artist = u''+tags[0]
        audiofile.tag.album = u''+tags[1]
        audiofile.tag.title = u''+tags[1]
    except IndexError:
        print('Tags may need revision.')
    finally:
        audiofile.tag.save()


def driver():
    init()
    url = command_line()
    mp4 = download(url)
    convert_mp4_to_mp3(mp4.title)
    update_tag(mp4.title)


if __name__ == '__main__':
    driver()

