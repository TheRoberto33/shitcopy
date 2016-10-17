import ModuleManager



class Player:

    def __init__(self):
        self.player = None
        self.volumecache = 1.0

    async def start(self, url):
        if self.player is not None:
            self.stop()
        print("Starting to play...")
        self.player = await ModuleManager.vclient().create_ytdl_player(url)
        print("go on...")
        self.player.start()
        self.player.volume = self.volumecache

    def stop(self):
        if self.player is not None:
            self.player.stop()
            self.player = None

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


player = Player()
