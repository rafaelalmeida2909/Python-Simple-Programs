import requests
from random import randint
import ctypes
import urllib
import os

value = randint(1000,2000)
link = "https://earthview.withgoogle.com/download/"+ str(value)+".jpg"
r = requests.get(link)

status = True
while status:
    if (r.status_code != 200):
        value = randint(1000,2000)
        link = "https://earthview.withgoogle.com/download/"+ str(value) +".jpg"
        r = requests.get(link)
    else:
        print(r.status_code)
        print(link)
        filename = os.getcwd() + "\wallpaper.jpg"
        print(filename)
        urllib.request.urlretrieve(link, filename)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filename , 0)
        status = False