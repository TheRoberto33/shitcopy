import ModuleManager



class Player:

    def __init__(self):
        self.player = None

    async def start(self, url):
        if self.player is not None:
            self.stop()
        print("Starting to play...")
        self.player = await ModuleManager.vclient().create_ytdl_player(url)
        print("go on...")
        self.player.start()


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
        if self.player is not None:
            self.player.volume = volume


player = Player()
