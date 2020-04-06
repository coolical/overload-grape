import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports

class Commands(client.Cog):
    def __init__(self, bot):
        self.b = bot

    @client.command(name='commands', description='displays available commands', help=f"{conf.prefix1}commands")#store command as command
    async def commands(self, ctx):
        e =discord.Embed(title="Commands", description="Here are all the commands/word/phrases you can use", color=conf.color)
        for command in self.b.commands:#iterates through command list and adds field with name and description
            e.add_field(name=command.name, value=command.description)
        for trigger in conf.triggers:#iterates through triggers and adds field with name and description
            e.add_field(name=trigger["key"], value=trigger["value"])
        await ctx.send(embed=e)#sends as embed

def setup(bot):
    bot.add_cog(Commands(bot))