import discord
import os
from discord.ext import commands
from config import BOT_TOKEN, BOT_PREFIX
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
import asyncpg


async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(database=DB_NAME, user=DB_USER, password=DB_PASS)

bot = commands.Bot(command_prefix=BOT_PREFIX)
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
    if filename.endswith('.py') and not filename.__contains__('init'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(
                f'cogs.{filename[:-3]}', error))

bot.loop.run_until_complete(create_db_pool())
bot.run(BOT_TOKEN)
