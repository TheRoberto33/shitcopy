import ModuleManager
import asyncio

from Player import player

#TODO: FInd sound files from somewhere and chooce from them randomly, since the whole song is a bit long
class EdfModule:

    async def on_message(self, message):
        if message.content.startswith("!EDF"):
            await player.start("https://youtu.be/SvbVNuBoBhg")

ModuleManager.addmodule(EdfModule())


