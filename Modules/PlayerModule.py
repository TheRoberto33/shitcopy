import ModuleManager
import asyncio
import SQLHelper

import discord

class PlayerModule:

    def __init__(self):
        self.player = None

    async def on_ready(self):
        pass

    async def on_message(self, message):
        text = message.content
        if text.startswith("!play "):
            text = "!player start" + text[5:]

        elif message.content.startswith("!player"):
            list = message.content.split()
            print(list)
            if len(list) == 1:
                return

            if list[1] == "start":
                if len(list) != 3:
                    return


                if not list[2].startswith("http"):
                    que = SQLHelper.query("SELECT url FROM YoutubeAliases WHERE alias=\'{0}\'".format(list[2]))
                    if que == None:
                        return
                    #SQL returns URL:s with '#' in front of them, idk why
                    for row in que:
                        list[2] = row.url[1:]
                        print(row.url[1:])



                self.player = await ModuleManager.vclient().create_ytdl_player(list[2])
                self.player.start()


            elif list[1] == "stop":
                if self.player != None:
                    self.player.stop()



ModuleManager.addmodule(PlayerModule())


