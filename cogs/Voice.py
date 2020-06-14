import discord
from discord.ext import commands
from discord.utils import get


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        try:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        except:
            await ctx.send(f'You have to join the voice channel')

    @commands.command()
    async def leave(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice:
            voice.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command()
    async def play(self, ctx):
        pass

    @commands.command()
    async def stop(self, ctx):
        pass


def setup(client):
    client.add_cog(Voice(client))
