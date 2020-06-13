import discord
import os
import json
from discord.ext import commands

with open("config.json") as config_file:
    config = json.load(config_file)
    TOKEN = config["bot_token"]
    PREFIX = config["bot_prefix"]

client = commands.Bot(command_prefix=PREFIX)


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

client.run(TOKEN)
