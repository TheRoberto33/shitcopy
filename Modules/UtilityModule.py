from Bot import bot
import importlib
from Player import player
class UtilityModule:

    async def on_message(self, message):
        print(message.author.name + ": " + message.content)






bot.addModule(UtilityModule())
