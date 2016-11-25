from Bot import bot


class GoogleModule:

    async def on_message(self, message):
        if message.content.startswith("!google"):
            words = message.content.split()[1:]
            # print("lmgtfy.com/?q=" + "+".join(words[1:]))
            await bot.client.send_message(message.channel, "http://www.lmgtfy.com/?q=" + "+".join(words))

        elif message.content.startswith("!actuallygoogle"):
            words = message.content.split()[1:]
            # print("lmgtfy.com/?q=" + "+".join(words[1:]))
            await bot.client.send_message(message.channel, "http://www.google.com/search?q=" + "+".join(words))


bot.addModule(GoogleModule())
