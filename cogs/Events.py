import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f'Ready: {self.client.user} | Servers: {len(self.client.guilds)}')

        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="test"))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(Events(client))
