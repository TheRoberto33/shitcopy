import ModuleManager
import asyncio
import SQLHelper

import time

import discord

class TestModule:


    async def on_ready(self):
        print(int(time.time()))
        pass

    async def on_message(self, message):

        print("INSERT INTO Messages(MessageID, Author, Content, Timestamp, ChannelID, HasAttachments, EditTImestamp) VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6});".format(message.id, message.author.name, message.content, int(time.time()), message.channel.id, False, "NULL"))

        SQLHelper.execcommit("INSERT INTO Messages(MessageID, Author, Content, Timestamp, ChannelID, HasAttachments, EditTImestamp) VALUES(?, ?, ?, ?, ?, ?, ?);", (message.id, message.author.name, message.content, int(time.time()), message.channel.id, False, "NULL"))

ModuleManager.addmodule(TestModule())


