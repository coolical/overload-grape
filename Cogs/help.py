import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf

class Help(client.Cog):
    def __init__(self, bot):
        self.b=bot
    @client.command(name='help', description='displays help text for commands', help=f"'{conf.prefix1}help <command name>' or '{conf.prefix1}help'")
    async def help(self,ctx,arg="NONE"):
        embed = discord.Embed(title="Help",description="Hello! I'm Arnold Palmer! Coolical dug up my dead body and injected my .chr file into discord! Here are the things I can do", color=conf.color)
        if arg=="NONE":#sends either general help or specified help
            for command in self.b.commands:
                embed.add_field(name=command.name, value=command.description)
            for trigger in conf.triggers:
                embed.add_field(name=trigger["key"], value=trigger['value'])
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