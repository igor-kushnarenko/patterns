import os
import pyglet


ABC_LIST = ['A', 'B', 'C']
DIG_LIST = ['1', '2', '3']

music_files = os.listdir('static')
music_list = [song.strip()[:-4] for song in music_files]


def songs_list(songs_list):
    songs = []
    for char in ABC_LIST:
        for dig in DIG_LIST:
            if len(songs_list) == 0:
                break
            songs.append(f'{char}{dig}. {songs_list.pop(0)}')
    return songs


songs = songs_list(music_list)
for song in songs:
    print(song)


choose = input()
for song in songs:
    if choose in song:
        for file in music_files:
            if song[4:] in file:
                song = pyglet.media.load(file)
                song.play()
                pyglet.app.run()

