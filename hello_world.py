import sys
from pprint import pprint as pp
from pytube import YouTube

pp(sys.path)

url = r'https://www.youtube.com/watch?v=xZAfdgYnsZc&list=PLYf3-nc0C5ly-2-7WU6S2nCW7MMT0VM87&index=2'
yt = YouTube(url)
print(yt.description)
