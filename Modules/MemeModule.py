from Bot import bot
import asyncio
import SQLHelper
import random

import ImgurAlbumParser



class MemeModule:

    async def on_message(self, message):
        if message.content.startswith("!meme"):
            mes = message.content.split()

            if len(mes) != 3:
                print("Meme request not dank enough")
                return


            que = SQLHelper.query("SELECT link FROM Memes WHERE type=? AND variant=?", (mes[1], mes[2]))

            if que == None:
                print("None...")
                return



            for q in que:
                print(q[0][-5:])
                if '.' in q[0][-5:]:
                    await bot.client.send_message(message.channel, q[0])

                else:
                    images = ImgurAlbumParser.getImages(q[0])
                    index = random.randint(0, len(images) - 1)
                    await bot.client.send_message(message.channel, images[index].link)
                    print(index)







            #await ModuleManager.client().send_message(message.channel, s)

bot.addModule(MemeModule())
