from html.parser import HTMLParser
import urllib.request
from imgurpython import ImgurClient


tokens = []

tokenfile = open("data/imgurtokens")
for line in tokenfile:
    tokens.append(line[:-1])
tokenfile.close()
client = ImgurClient(tokens[0], tokens[1])




def getImages(url):

    return client.get_album_images(url[(len(url) - 5):])
