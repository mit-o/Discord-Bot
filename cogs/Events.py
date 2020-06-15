import discord
from discord.ext import commands
import asyncio


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def status_task(self):
        while True:
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='!help'))
            await asyncio.sleep(20)
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'with {len(self.client.users)} users'))
            await asyncio.sleep(20)
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'on {len(self.client.guilds)} servers'))
            await asyncio.sleep(20)

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f'Ready: {self.client.user} | Servers: {len(self.client.guilds)}')
        self.client.loop.create_task(self.status_task())


def setup(client):
    client.add_cog(Events(client))
