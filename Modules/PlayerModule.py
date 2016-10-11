import ModuleManager
import asyncio
import SQLHelper

import discord

from Player import player

class PlayerModule:


    async def on_ready(self):
        pass

    async def on_message(self, message):
        text = message.content
        if text.startswith("!play "):
            text = "!player start" + text[5:]
            print(text)

        if text.startswith("!stfu"):
            text = "!player stop"

        if text.startswith("!player"):
            list = text.split()
            print(list)
            if len(list) == 1:
                return

            if list[1] == "start":
                if len(list) != 3:
                    return


                if not list[2].startswith("http"):
                    que = SQLHelper.query("SELECT url FROM YoutubeAliases WHERE alias=\'{0}\'".format(list[2]))
                    if que is None:
                        return
                    #SQL returns URL:s with '#' in front of them, idk why
                    for row in que:
                        list[2] = row[0][1:]
                        print(row[0][1:])


                if "&" in list[2]:
                    index = list[2].index("&")
                    list[2] = list[2][:index - 1]

                await player.start(list[2])


            elif list[1] == "stop":
                player.stop()


            elif list[1] == "pause":
                player.pause()

            elif list[1] == "resume":
                player.resume()

            elif list[1] == "volume":
                if self.player is not None and len(list) == 3:
                    try:
                        if list[2].endswith("%"):
                            list[2] = list[2][:-1]
                        player.volume(float(int(list[2])) / 100.0)
                    except TypeError:
                        pass



ModuleManager.addmodule(PlayerModule())


