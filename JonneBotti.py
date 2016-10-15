import discord

import asyncio
import os
import importlib
import ModuleManager
import SQLHelper
import ImgurAlbumParser

client = discord.Client()

discord.opus.load_opus("libopus.so")

ModuleManager.initManager(client)


SQLHelper.init()


ImgurAlbumParser.init()

# Automatically imports anything that is named *Module.py
s = os.path.realpath(__file__)
s = s[:(len(s) - 13)] + "Modules/"
for file in os.listdir(s):
    if file.endswith(".py") and file[:(len(file) - 3)].endswith("Module"):
        importlib.import_module("Modules." + file[:(len(file) - 3)])
        print("Imported: {0}".format(file))


@client.event
async def on_ready():
    for c in client.get_all_channels():
        if c.id == "199174130296160257":
            try:
                pass
                #voice = await client.join_voice_channel(c)
                #ModuleManager.initVoice(voice)
            except asyncio.TimeoutError:
                print("timeouterror")
            except discord.ClientException:
                print("clientexception")
            # ModuleManager.initVoice(voice)
            ModuleManager.initVoice(None)
    import Player

    print('Logged in!')
    print("Modules: ")
    print(len(ModuleManager.modules()))
    print('------')

    for m in ModuleManager.modules():
        try:
            await m.on_ready()
        except AttributeError:
            pass


@client.event
async def on_message(message):
    # No self-answering
    if message.author == client.user:
        return

    for m in ModuleManager.modules():
        try:
            await m.on_message(message)
        except AttributeError:
            pass

    if message.content == "!kill":
        await ModuleManager.vclient().disconnect()
        exit()


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    for m in ModuleManager.modules():
        try:
            await m.on_message_delete(message)
        except AttributeError:
            pass


@client.event
async def on_message_edit(before, after):
    if after.author == client.user:
        return

    for m in ModuleManager.modules():
        try:
            await m.on_message_edit(before, after)
        except AttributeError:
            pass

tokenfile = open("data/token.txt", "r")

client.run(tokenfile.read())

tokenfile.close()
