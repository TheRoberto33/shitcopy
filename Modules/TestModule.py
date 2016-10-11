import ModuleManager
import asyncio
import SQLHelper

import discord

class TestModule:


    async def on_ready(self):
        pass

    async def on_message(self, message):
        if message.content.startswith("!sql"):
            que = SQLHelper.query(message.content[5:])
            if que != None:
                for row in que:
                    print(row.link)



ModuleManager.addmodule(TestModule())


