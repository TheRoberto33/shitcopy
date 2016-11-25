from Bot import bot

class LennyModule:

    def is_int(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    def repeatstr(self, str, num):
        result = ""
        for i in range(0, num):
            result += str + " "
        return str


    async def on_message(self, message):
        if message.content.startswith("!lenny"):
            mes = message.content.split()
            if len(mes) == 1:
                await bot.client.send_message(message.channel, "( ͡° ͜ʖ ͡°)")

            elif len(mes) == 2 and self.is_int(mes[1]):
                num = int(mes[1])
                if num <= 0 or 100 < num:
                    return
                result = ""
                for i in range(0, int(mes[1])):
                    if i % 10 == 0:
                        result += "\n"
                    result += "( ͡° ͜ʖ ͡°) "
                await bot.client.send_message(message.channel, result)


bot.addModule(LennyModule())
