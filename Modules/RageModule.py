from Bot import bot
import SQLHelper
import random

class RageModule:



    async def on_message(self, message):
        if message.author.name == "The_Roberto" or message.content.startswith("!roope"):
            print("Roope said: " + message.content)

            # Damn, that's self documenting. Wait, I'm writing a comment. Shit.
            shouldBeActedUpon = False

            # TODO: Is this enough?
            animeTriggers = ["anime", "animu"]

            for x in animeTriggers:
                if x + " " in message.content.lower() or " " + x in message.content.lower():
                    shouldBeActedUpon = True


            if any(message.content.lower().endswith(x) for x in animeTriggers):
                shouldBeActedUpon = True





            if shouldBeActedUpon:
                        SQL = "SELECT text,probability FROM AnimeRage"

                        que = SQLHelper.query(SQL)

                        sumquery = SQLHelper.query("SELECT SUM(probability) FROM AnimeRage")

                        nullquery = SQLHelper.query("SELECT SUM(case when probability is null then 1 end) FROM AnimeRage")

                        probsum = float(sumquery[0][0])

                        if probsum > 1.0 or (probsum == 1 and nullquery[0] != 0):
                            await bot.client.send_message(message.channel, "Rage towards Roope was so great that it caused an error. No, seriously, there's an error with SQL")
                            return

                        if nullquery[0][0] is not 0:
                            nullprob = (1.0 - probsum) / float(nullquery[0][0])
                        else:
                            nullprob = 0.0

                        rand = random.random()

                        currentsum = 0.0


                        for row in que:

                            if row[1] is None:
                                currentsum += nullprob
                            else:
                                currentsum += row[1]
                            if rand < currentsum:
                                await bot.client.send_message(message.channel, row[0])
                                break








bot.addModule(RageModule())
