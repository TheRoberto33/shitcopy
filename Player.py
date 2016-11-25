from Bot import bot
import asyncio
from time import sleep

class Player:

    def __init__(self):
        self.player = None
        self.volumecache = 1.0
        self.playAgain = asyncio.Event()
        self.rep = False
        self.queue = []
        self.task = bot.client.loop.create_task(self.player_task())
        self.currentlyplaying = None

    def gotonext(self):
        self.currentlyplaying = None
        bot.client.loop.call_soon_threadsafe(self.playAgain.set)

    def addToQueue(self, url):
        self.queue.append(url)

    def clearQueue(self):
        self.queue = []



    def removeFromQueue(self, index):
        try:
            del self.queue[index]
        except:
            pass

    def setQueue(self, que):
        self.queue = que

    def repeat(self):
        self.rep = True
        if self.player is not None and self.player.is_playing():
            self.queue = [self.currentlyplaying,] + self.queue

    def dontrepeat(self):
        self.rep = False

    def isRepeating(self):
        return self.rep

    async def start(self):
        if self.player is not None and self.player.is_playing():
            return
        if len(self.queue) == 0:
            return

        print(bot.vclient)
        self.player = await bot.vclient.create_ytdl_player(self.queue[0], use_avconv=False, after=self.gotonext)
        self.player.volume = self.volumecache
        self.player.start()
        self.currentlyplaying = self.queue[0]
        if not self.rep:
            self.queue = self.queue[1:]


    async def stop(self):
        if self.player is not None and self.player.is_playing():
            self.rep = False
            self.queue = []
            self.player.stop()
            self.player = None
            await self.playAgain.wait()

    def pause(self):
        if self.player is not None:
            self.player.pause()

    def resume(self):
        if self.player is not None:
            self.player.resume()

    #Range 0.0 - 2.0
    def volume(self, volume):
        volume = max(min(volume, 2.0), 0.0)
        self.volumecache = volume
        if self.player is not None:
            self.player.volume = volume


    async def player_task(self):
        while True:
            self.playAgain.clear()
            await self.playAgain.wait()
            await self.start()

player = Player()
