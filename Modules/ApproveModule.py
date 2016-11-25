from Bot import bot


class ApproveModule:

    def __init__(self):
        self.stamps = {
            "The_Roberto": "RobertoSeal.png",
            "Shootingderp": "ShootingderpSeal.png",
            "Sir_Failius_Noobius": "SirFailiusNoobiusSeal.png",
            "Heiski": "HeiskiSeal.png"
            }

    async def on_message(self, message):
        if message.content.startswith("!approve"):
            f = None
            try:
                f = self.stamps[message.author.name]
            except:
                pass

            try:
                await bot.client.delete_message(message)
            except:
                pass

            if f is not None:
                await bot.client.send_file(message.channel, "data/" + f)




bot.addModule(ApproveModule())
