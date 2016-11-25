from Bot import bot
import SQLHelper
from Player import player
from time import sleep
# Plays youtube videos
class PlayerModule:

    async def on_ready(self):
        pass

    # Makes all youtube url:s usable(yes, even playlists)
    def processUrl(self, url):
        if "youtu" not in url:
            return None

        if url.startswith("www") or url.startswith("youtu.be"):
            url = "https://" + url

        if '&' in url:
            index = url.index("&")
            url = url[:index]

        if 'list' in url:
            index = url.inedex('list')
            url = url[:index]

        return url

    async def on_message(self, message):
        text = message.content

        # For ease of use
        if text.startswith("!play "):
            text = "!player start" + text[5:]

        if text.startswith("!stfu"):
            text = "!player stop"

        if text.startswith("!repeat"):
            text = "!player repeat"

        if text.startswith("!playlater"):
            text = "!player queue add " + text[11:]

        if text.startswith("!skip"):
            text = "!player skip"

        # The actual handling of commands
        if text.startswith("!player"):
            mes = text.split()
            if len(mes) == 1:
                return

            if mes[1] == "start":
                if len(mes) != 3:
                    return

                # If it is an alias
                if not mes[2].startswith("http"):
                    que = SQLHelper.query("SELECT url FROM YoutubeAliases WHERE alias=?", (mes[2],))
                    if len(que) == 0:
                        return
                    mes[2] = que[0][0]

                url = self.processUrl(mes[2])
                if url is None:
                    return
                print("PLAY " + url)
                await player.stop()
                player.addToQueue(url)
                await player.start()


            elif mes[1] == "stop":
                await player.stop()

            elif mes[1] == "repeat":
                if len(mes) == 2:
                    player.repeat()
                elif len(mes) == 3:
                    if(mes[2] == "on"):
                        player.repeat()
                    elif(mes[2] == "off"):
                        player.dontrepeat()

            elif mes[1] == "skip":
                player.skip()

            elif mes[1] == "pause":
                player.pause()

            elif mes[1] == "resume":
                player.resume()

            elif mes[1] == "volume":
                    if player.player is not None and len(mes) == 3:
                        try:
                            if mes[2].endswith("%"):
                                mes[2] = mes[2][:-1]
                            player.volume(float(int(mes[2])) / 100.0)
                        except:
                            pass

            elif mes[1] == "print":

                globals = SQLHelper.query("SELECT alias FROM YoutubeAliases WHERE submitter is NULL")
                personals = SQLHelper.query("SELECT alias FROM YoutubeAliases WHERE submitter=?", (message.author.name,))

                result = "**Globals:**\n"
                for al in globals:
                    result += al[0] + "\n"

                result += "**Personals:**\n"

                for al in personals:
                    result += al[0] + "\n"

                await bot.client.send_message(message.author, result)

            elif mes[1] == "add":
                # Error in command, delete it before exiting
                if len(mes) != 4:
                    try:
                        await bot.client.delete_message(message)
                    except:
                        await bot.client.send_message(message.channel, "Poistaisin jos ois luvat")
                    return

                # Error in url, delete it before exiting
                url = self.processUrl(mes[3])
                if url is None:
                    try:
                        await bot.client.delete_message(message)
                    except:
                        await bot.client.send_message(message.channel, "Poistaisin jos ois luvat")
                    return

                submitter = SQLHelper.query("SELECT submitter FROM YoutubeAliases WHERE alias=?", (mes[2],))

                # If nobody has taken the alias
                if len(submitter) == 0:
                    SQLHelper.execcommit("INSERT INTO YoutubeAliases VALUES(NULL, ?, ?, ?);", (mes[2], url, message.author.name))
                else:
                    if submitter[0][0] == message.author.name:
                        SQLHelper.execcommit("UPDATE YoutubeAliases SET url=? WHERE alias=?", format(url, mes[2],))

                    else:
                        await bot.client.send_message(message.channel, "Sori, joku muu oli jo ottanu ton lyhenteen :/")
                try:
                    await bot.client.delete_message(message)
                except:
                    await bot.client.send_message(message.channel, "Poistaisin jos ois luvat")

            # Move video from personals to globals
            elif mes[1] == "promote":
                if len(mes) != 3 or message.author.name != "Heiski":
                    return

                SQLHelper.execcommit("UPDATE YoutubeAliases SET submitter=NULL WHERE alias=?", (mes[2],))


            elif mes[1] == "queue":
                if len(mes) < 3:
                    return

                elif mes[2] == "add" and len(mes) == 4:
                        # If it is an alias
                    if not mes[3].startswith("http"):
                        que = SQLHelper.query("SELECT url FROM YoutubeAliases WHERE alias=?", (mes[3],))
                        if len(que) == 0:
                            return
                        mes[3] = que[0][0]

                    url = self.processUrl(mes[3])
                    if url is None:
                        return
                    player.addToQueue(url)

                elif mes[2] == "clear":
                    player.clearQueue()

                elif mes[2] == "pop":
                    player.removeFromQueue(len(player.queue) - 1)

                elif mes[2] == "remove" and len(mes) == 4:
                    try:
                        index = int(mes[3])
                        if index >= len(player.queue):
                            player.removeFromQueue(index)
                    except:
                        pass

                elif mes[2] == "print":
                    res = ""

                    for i in range(0, len(player.queue)):
                        res += str(i) + ". " + player.queue[i] + "\n"
                    await bot.client.send_message(message.channel, res)





            elif mes[1] == "remove":
                if len(mes) != 3:
                    return
                if message.author.name != "Heiski":
                    SQLHelper.execcommit("DELETE FROM YoutubeAliases WHERE alias=? and submitter=?", (mes[2], message.author.name))
                else:
                    SQLHelper.execcommit("DELETE FROM YoutubeAliases WHERE alias=?", (mes[2],))

            elif mes[1] == "help":
                f = open("data/playerhelp.txt", "r")
                await bot.client.send_message(message.channel, f.read())
                f.close()

            else:
                await bot.client.send_message(message.channel, "Mitä vittua sä jätkä horiset? *!player help* vois auttaa...")



bot.addModule(PlayerModule())
