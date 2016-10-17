import ModuleManager
import importlib

class UtilityModule:

    async def on_message(self, message):
        if message.content.startswith("!reload"):
            words = message.content.split()
            # print("lmgtfy.com/?q=" + "+".join(words[1:]))
            # importlib.reload(words[1])
            await ModuleManager.client().send_message(message.channel, "No. Not yet, at least")
        elif message.content.startswith("!say") and message.channel == "233591578583760896":
            await ModuleManager.client().send_message(message.content[5:23], message.content[23:])


ModuleManager.addmodule(UtilityModule())
