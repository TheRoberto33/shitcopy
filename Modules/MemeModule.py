import ModuleManager
import asyncio
import SQLHelper
import random

import ImgurAlbumParser



class MemeModule:

    async def on_message(self, message):
        if message.content.startswith("!meme"):
            list = message.content.split()

            if len(list) != 3:
                print("Meme request not dank enough")
                return

            SQL = "SELECT link FROM Memes WHERE type=\'{0}\' AND variant=\'{1}\'".format(list[1], list[2]);
            print(SQL)
            que = SQLHelper.query(SQL)

            if que == None:
                print("None...")
                return


            for q in que:
                if '.' in q.link[(len(q.link) - 5):]:
                    await ModuleManager.client().send_message(message.channel, q.link)

                else:
                    images = ImgurAlbumParser.getImages(q.link)
                    index = random.randint(0, len(images) - 1)
                    await ModuleManager.client().send_message(message.channel, images[index].link)
                    print(index)






            #await ModuleManager.client().send_message(message.channel, s)

ModuleManager.addmodule(MemeModule())


