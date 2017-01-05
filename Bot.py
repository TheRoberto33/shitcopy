import discord
import json
client = discord.Client();
class Bot:
    def __init__(self):
        self.client = client
        discord.opus.load_opus("libopus.dll")
        self.vclient = None
        self.modules = []
        self.arguments = {}
        self.arguments["vchannel"] = "Things"



    def run(self, arguments):
        self.arguments = {**self.arguments, **arguments}

        tokenfile = open("data/token.txt", "r")
        client.run(tokenfile.read())
        tokenfile.close()

    def addModule(self, module):
        self.modules.append(module)

bot = Bot()

@client.event
async def on_ready():
    for c in client.get_all_channels():
        channelfile = open("data/channels")
        parsed = json.loads(channelfile.read())
        channelfile.close()
        if c.id == parsed[bot.arguments["vchannel"]]:
            try:
                bot.vclient = await client.join_voice_channel(c)
                break
            except asyncio.TimeoutError:
                print("timeouterror")
            except discord.ClientException:
                print("clientexception")
    print('Voice connected, all ready!')
    print("Modules: ")
    print(len(bot.modules))
    print('--------------------')

    for m in bot.modules:
        try:
            await m.on_ready()
        except AttributeError:
            pass


@client.event
async def on_message(message):
    # No self-answering
    if message.author == client.user:
        return
    for m in bot.modules:
        try:
            await m.on_message(message)
        except AttributeError:
            pass


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return
    for m in bot.modules:
        try:
            await m.on_message_delete(message)
        except AttributeError:
            pass


@client.event
async def on_message_edit(before, after):
    if after.author == client.user:
        return
    for m in bot.modules:
        try:
            await m.on_message_edit(before, after)
        except AttributeError:
            pass
