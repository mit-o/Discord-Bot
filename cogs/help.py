from discord import Embed
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.command()
    async def help(self, ctx):
        embed = Embed(
            description="""To view the commands in each group use:
			```!help <group>```""",
            color=0xf257b0
        )

        embed.set_author(
            name="Turtle's commands.",
            icon_url=ctx.guild.me.avatar_url)

        embed.set_thumbnail(
            url=ctx.guild.me.avatar_url)

        embed.add_field(name='Author: ', value='Mito#4430')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
