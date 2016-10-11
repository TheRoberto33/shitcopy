import ModuleManager
import asyncio

#Module that repeats a message if a number of seperate users say it back to back(multiple messages from one user will not break the chain)
#All images, links and commands are ignored and will break the chain
#Case is ignored, punctuation at the end of the message is ignored
#For example: Roope: (Kuva)    Heikki: Ei    Aplu: ei    Oliver: EI!    JonneBotti: ei
class TestModule:

    def __init__(self, neededUsers):
        self.users = []
        self.text = ""
        self.neededUsers = neededUsers

    def parseString(self, toparse):
        toparse = toparse.upper()
        toparse = toparse.strip()
        for i, e in reversed(list(enumerate(toparse))):
            if e not in ['.', ',', '!', '?']:
                break
            toparse = toparse[:i] + toparse[(i + 1):]


        return toparse

    async def on_ready(self):
        pass

    async def on_message(self, message):
        if message.content.startswith("!") or len(message.embeds) != 0 or len(message.attachments) != 0:
            self.users = []
            self.text = ""
            return


        if self.parseString(message.content) != self.text:
            self.text = self.parseString(message.content)
            self.users = []
            self.users.append(message.author.name)
            return


        if message.author.name not in self.users or True:
            self.users.append(message.author.name)

            if len(self.users) == 3:
                self.users = []
                await ModuleManager.client().send_message(message.channel, self.text.lower())








ModuleManager.addmodule(TestModule(2))


