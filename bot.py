# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # from .env file
client = commands.Bot(command_prefix='!')


# status check
@client.event
async def on_ready(ctx):
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
