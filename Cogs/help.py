import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf

class Help(client.Cog):
    def __init__(self, bot):
        self.b=bot
    @client.command(name='help', description='Displays help text for commands', help=f"'{conf.prefix1}help <command name>' or '{conf.prefix1}help'")
    async def help(self,ctx,arg="NONE"):
        if arg=="NONE":#sends either general help or specified help
            embed = discord.Embed(title="Help",description="Hello! I'm Arnold Palmer! Coolical dug up my cold dead body and injected my .chr file into Discord! Here are the things I can do:", color=conf.color)
            for command in self.b.commands:
                embed.add_field(name=f"{conf.prefix1}{command.name}", value=command.description)
            for trigger in conf.triggers:
                embed.add_field(name=trigger["key"], value=trigger['value'])
        else:            
            try:
                embed = discord.Embed(title="Help",description="Here is the usage", color=conf.color)
                command = self.b.get_command(arg)
                embed.add_field(name=command.name, value=command.help)
            except:
                await ctx.send(f"`{arg}` is not a command. Maybe try without `{conf.prefix1}`?")
                return
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))