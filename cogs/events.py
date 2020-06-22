import discord
from discord.ext import commands
import asyncio


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def status_task(self):
        while True:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='!help'))
            await asyncio.sleep(20)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'with {len(self.bot.users)} users'))
            await asyncio.sleep(20)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'on {len(self.bot.guilds)} servers'))
            await asyncio.sleep(20)

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f'Ready: {self.bot.user} | Servers: {len(self.bot.guilds)}')
        self.bot.loop.create_task(self.status_task())
        self.bot.appinfo = await self.bot.application_info()


def setup(bot):
    bot.add_cog(Events(bot))
