from Bot import bot
import asyncio
import SQLHelper

import time

import discord

class TestModule:


    async def on_ready(self):
        print(int(time.time()))
        pass

    async def on_message(self, message):
        SQLHelper.execcommit("INSERT INTO Messages(MessageID, Author, Content, Timestamp, ChannelID, HasAttachments, EditTImestamp) VALUES(?, ?, ?, ?, ?, ?, ?);", (message.id, message.author.name, message.content, int(time.time()), message.channel.id, False, "NULL"))

bot.addModule(TestModule())
