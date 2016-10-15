import ModuleManager
import importlib

class UtilityModule:

    async def on_message(self, message):
        if message.content.startswith("!reload"):
            words = message.content.split()
            # print("lmgtfy.com/?q=" + "+".join(words[1:]))
            # importlib.reload(words[1])
            await ModuleManager.client().send_message(message.channel, "No. Not yet, at least")



ModuleManager.addmodule(UtilityModule())
