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

            elif list[1] == "alias":
                if len(list) == 2:
                    return

                if list[2] == "print":

                    if len(list) == 4 and list[3] == "personal":
                        que = SQLHelper.query("SELECT alias FROM YoutubeAliases WHERE submitter=\'{0}\'".format(message.author.name))
                    else:
                        que = SQLHelper.query("SELECT alias FROM YoutubeAliases WHERE submitter is NULL")

                    if len(que) == 0:
                        return
                    result = ""
                    for al in que:
                        result += al[0] + " "

                    await ModuleManager.client().send_message(message.channel, result)

                elif list[2] == "add":
                    if len(list) != 5:
                        return

                    url = self.processUrl(list[4])
                    if url is None:
                        return


                    que = SQLHelper.query("SELECT submitter FROM YoutubeAliases WHERE alias=\'{0}\'".format(list[3]))

                    if len(que) == 0:
                        SQLHelper.execcommit("INSERT INTO YoutubeAliases VALUES(NULL, ?, ?, ?);", (list[3], list[4], message.author.name))
                    else:
                        sub = que[0][0]
                        if sub == message.author.name:
                            SQLHelper.execcommit("UPDATE YoutubeAliases SET url=\'{0}\' WHERE alias=\'{1}\'".format(list[4], list[3]))
                        else:
                            await ModuleManager.client().send_message(message.channel, "No. Bad dog.")






ModuleManager.addmodule(PlayerModule())
