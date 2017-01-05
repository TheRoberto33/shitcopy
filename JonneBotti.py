import asyncio
import os
import importlib
import SQLHelper
import ImgurAlbumParser

from Bot import bot


# Automatically imports anything that is named *Module.py
s = os.path.realpath(__file__)
s = s[:(len(s) - 13)] + "Modules/"
for file in os.listdir(s):
    if file.endswith(".py") and file[:(len(file) - 3)].endswith("Module"):
        importlib.import_module("Modules." + file[:(len(file) - 3)])
        print("Imported: {0}".format(file))


bot.run({"vchannel": "Things"})
