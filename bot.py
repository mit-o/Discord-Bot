import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(
                f'cogs.{filename[:-3]}', error))

'''
# status check
@client.event
async def on_ready(ctx):
    print(f'{client.user} has connected to Discord!')

'''
client.run(TOKEN)
