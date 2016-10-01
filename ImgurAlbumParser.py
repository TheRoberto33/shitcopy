
from html.parser import HTMLParser

import urllib.request

from imgurpython import ImgurClient

def init():
    global __client
    __client = ImgurClient("a5c8b43111a04e2", "a74daf33a4179108220a5f037abcde1071f7985b")



def getImages(url):

    return __client.get_album_images(url[(len(url) - 5):])



