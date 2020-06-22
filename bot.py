import discord
import os
import json
from discord.ext import commands

with open("config.json") as config_file:
    config = json.load(config_file)
    TOKEN = config["bot_token"]
    PREFIX = config["bot_prefix"]

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command("help")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(
                f'cogs.{filename[:-3]}', error))

bot.run(TOKEN)
