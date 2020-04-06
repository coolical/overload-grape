import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf

class Help(client.Cog):
    def __init__(self, bot):
        self.b=bot
    @client.command(name='help', description='displays help text for commands', help=f"'{conf.prefix1}help <command name>' or '{conf.prefix1}help'")
    async def help(self,ctx,arg="NONE"):
        embed = discord.Embed(title="Help", color=conf.color)
        if arg=="NONE":#sends either general help or specified help
            for command in self.b.commands:
                embed.add_field(name=command.name, value=command.help)
        else:            
            try:
                command = self.b.get_command(arg)
                embed.add_field(name=command.name, value=command.help)
            except:
                await ctx.send(f"{arg} is not a command")
                return
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))