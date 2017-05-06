
import os,subprocess
my_path = '/home/tushar/Music/Devotional/'
songs_list = os.listdir(my_path)
song_str = ''
for song in songs_list:
    subprocess.run(["mpv", my_path+song])
#subprocess.run(["cvlc", "/home/tushar/PycharmProjects/Morning Devotional Songs/Ganesha.opus"])