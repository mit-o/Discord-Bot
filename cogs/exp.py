import discord
from discord.ext import commands
import asyncpg
import asyncio
from random import randint


class Exp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def process_xp(self, message):
        author_id = message.author.id
        guild_id = message.guild.id

        user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE id = $1", author_id)
        if not user:
            await self.bot.pg_con.execute("INSERT INTO users (id) VALUES ($1)", author_id)

        exp = await self.bot.pg_con.fetch("SELECT * FROM exp WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
        if not exp:
            await self.bot.pg_con.execute("INSERT INTO exp (user_id, guild_id) VALUES ($1, $2)", author_id, guild_id)

        exp = await self.bot.pg_con.fetchrow("SELECT * FROM exp WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)

        await self.add_xp(message, exp['exp'], exp['level'])

    @commands.Cog.listener()
    async def add_xp(self, message, xp, lvl):
        author_id = message.author.id
        guild_id = message.guild.id

        xp_to_add = randint(10, 20)
        new_lvl = int(((xp + xp_to_add) // 42) ** 0.55)

        exp = await self.bot.pg_con.fetchrow("SELECT * FROM exp WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
        await self.bot.pg_con.execute("UPDATE exp SET exp = $1, level = $2 WHERE user_id = $3 AND guild_id = $4", exp['exp'] + xp_to_add, new_lvl, author_id, guild_id)

        if new_lvl > exp['level']:
            await message.channel.send(f"Congrats {message.author.mention} - you reached level {new_lvl:,}!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            await self.process_xp(message)


def setup(bot):
    bot.add_cog(Exp(bot))
