import ModuleManager
import asyncio

class LennyModule:

    async def on_message(self, message):
        if message.content.startswith("!lenny"):
            await ModuleManager.client().send_message(message.channel, "( ͡° ͜ʖ ͡°)")

ModuleManager.addmodule(LennyModule())


