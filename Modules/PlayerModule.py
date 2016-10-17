import ModuleManager
import SQLHelper
from Player import player


class PlayerModule:

    async def on_ready(self):
        pass

    def processUrl(self, url):
        if "youtu" not in url:
            return None

        if url.startswith("www") or url.startswith("youtu.be"):
            url = "https://" + url

        if "&" in url:
            index = url.index("&")
            url = url[:index - 1]
        if "?" in url:
            index = url.index("?")
            url = url[:index - 1]
        return url

    async def on_message(self, message):
        text = message.content
        if text.startswith("!play "):
            text = "!player start" + text[5:]
            print(text)

        if text.startswith("!stfu"):
            text = "!player stop"

        if text.startswith("!player"):
            list = text.split()
            if len(list) == 1:
                return



            if list[1] == "start":
                if len(list) != 3:
                    return

                if not list[2].startswith("http"):
                    que = SQLHelper.query("SELECT url FROM YoutubeAliases WHERE alias=\'{0}\'".format(list[2]))
                    if len(que) == 0:
                        return
                    list[2] = que[0][0]

                url = self.processUrl(list[2])
                if url is None:
                    return

                await player.start(list[2])



            elif list[1] == "stop":
                player.stop()

            elif list[1] == "pause":
                player.pause()

            elif list[1] == "resume":
                player.resume()

            elif list[1] == "volume":
                    if player.player is not None and len(list) == 3:
                        try:
                            if list[2].endswith("%"):
                                list[2] = list[2][:-1]
                            player.volume(float(int(list[2])) / 100.0)
                        except:
                            pass


            elif list[1] == "print":

                if len(list) == 3 and list[2] == "personal":
                    que = SQLHelper.query("SELECT alias FROM YoutubeAliases WHERE submitter=\'{0}\'".format(message.author.name))
                else:
                    que = SQLHelper.query("SELECT alias FROM YoutubeAliases WHERE submitter is NULL")

                if len(que) == 0:
                    return
                result = ""
                for al in que:
                    result += al[0] + " "

                await ModuleManager.client().send_message(message.channel, result)

            elif list[1] == "add":
                if len(list) != 4:
                    try:
                        await ModuleManager.client().delete_message(message)
                    except:
                        await ModuleManager.client().send_message(message.channel, "Poistaisin jos ois luvat")
                    return

                url = self.processUrl(list[3])
                if url is None:
                    try:
                        await ModuleManager.client().delete_message(message)
                    except:
                        await ModuleManager.client().send_message(message.channel, "Poistaisin jos ois luvat")
                    return


                que = SQLHelper.query("SELECT submitter FROM YoutubeAliases WHERE alias=\'{0}\'".format(list[2]))

                if len(que) == 0:
                    SQLHelper.execcommit("INSERT INTO YoutubeAliases VALUES(NULL, ?, ?, ?);", (list[2], list[3], message.author.name))
                else:
                    sub = que[0][0]
                    if sub == message.author.name:
                        SQLHelper.execcommit("UPDATE YoutubeAliases SET url=\'{0}\' WHERE alias=\'{1}\'".format(list[3], list[2]))

                    else:
                        await ModuleManager.client().send_message(message.channel, "Sori, joku muu oli jo ottanu ton lyhenteen :/")
                try:
                    await ModuleManager.client().delete_message(message)
                except:
                    await ModuleManager.client().send_message(message.channel, "Poistaisin jos ois luvat")

            elif list[1] == "promote":
                if len(list) != 3 or message.author.name != "Heiski":
                    return

                SQLHelper.execcommit("UPDATE YoutubeAliases SET submitter=NULL WHERE alias=\'{1}\'".format(list[2]))


            elif list[1] == "help":
                f = open("data/playerhelp.txt", "r")
                await ModuleManager.client().send_message(message.channel, f.read())
                f.close()

            else:
                await ModuleManager.client().send_message(message.channel, "Mitä vittua sä jätkä horiset? *!player help* vois auttaa...")



ModuleManager.addmodule(PlayerModule())
