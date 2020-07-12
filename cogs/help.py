import discord
from discord.ext import commands
from config import COG_EXCEPTION


class CustomHelp(commands.Cog, name='Help'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *cog):
        """Gets all cogs and commands."""

        if not cog:

            embed = discord.Embed(
                description="""
                To view what certain command do, use:
                ***!help <command>***
                """,
                color=0x437840
            )
            embed.set_author(name="Turtle's commands.",
                             icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=f"Author: {self.bot.appinfo.owner}",
                             icon_url='https://cdn.discordapp.com/attachments/596341948705407040/724748657924112454/610021821856743444.gif')

            for x in self.bot.cogs:
                if x in COG_EXCEPTION or len(self.bot.cogs[x].get_commands()) == 0:
                    pass
                else:
                    cogs_cmds = self.bot.cogs[x].get_commands()
                    f_cogs_cmds = '\n'.join(
                        (["✧ " + c.name for c in cogs_cmds]))

                    embed.add_field(
                        name=x, value=f'{f_cogs_cmds}', inline=True)
            await ctx.send(embed=embed)
        else:
            if len(cog) > 1:
                embed = discord.Embed(
                    title='Error!', description='Too many cogs!', color=0x437840)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.set_footer(
                    text=f"Author: {self.bot.appinfo.owner}", icon_url=self.bot.user.avatar_url)

                await ctx.message.author.send('', embed=embed)
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            embed = discord.Embed(color=0x437840)
                            scog_info = ''
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    scog_info += f'**{c.name}** - {c.help}\n'
                            embed.add_field(
                                name=f'{cog[0]} Module - {self.bot.cogs[cog[0]].__doc__}', value=scog_info)
                            embed.set_footer(
                                text=f"Author: {self.bot.appinfo.owner}",
                                icon_url=self.bot.user.avatar_url)
                            found = True
            if not found:
                for x in self.bot.cogs:
                    for c in self.bot.get_cog(x).get_commands():

                        if c.name == cog[0]:
                            embed = discord.Embed(color=0x437840)
                            embed.add_field(
                                name=f'{c.name} - {c.help}', value=f'Proper Syntax:\n`{c.qualified_name} {c.signature}`')
                            embed.set_footer(
                                text=f"Author: {self.bot.appinfo.owner}",
                                icon_url=self.bot.user.avatar_url)

                    found = True
                if not found:
                    embed = discord.Embed(
                        title='Error!', description='How do you even use "'+cog[0]+'"?', color=0x437840)
                else:
                    pass
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, 'on_error'):
                return
            else:
                embed = discord.Embed(
                    title=f'Error in {ctx.command}', description=f'`{ctx.command.qualified_name} {ctx.command.signature}` \n{error}', color=0x43788)
                embed.set_thumbnail(url=self.bot.user.avatar_url)

                await ctx.send(embed=embed)
                await ctx.message.add_reaction(emoji='❔')
        except:
            embed = discord.Embed(
                title=f'Error in {ctx.command}',
                description=f'{error}',
                color=0x43788
            )

            embed.set_thumbnail(url=self.bot.user.avatar_url)

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CustomHelp(bot))
