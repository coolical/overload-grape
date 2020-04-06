import discord, random, asyncio, random
from discord.ext import commands as client
from Cogs.config import conf
embed = discord.Embed(title="You're going to have a bad time", color=conf.color)
embed.set_image(url="http://i.imgur.com/3rRJp4q.jpg")
choices = ["Hey that's not nice", embed, 'You called?']
conf.triggers.append({"key":"fuck arnold palmer", "value":"Why would you do that?"})
class Fap(client.Cog):
    def __init__(self, bot):
        self.b = bot
    
    @client.Cog.listener()
    async def on_message(self, message):
        if 'fuck arnold palmer' in message.content.lower() and not message.author.bot:#checks if bot and if trigger is said
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            chosen = random.choice(choices)
            if isinstance(chosen, str):#sends choice as repective type
                await message.channel.send(chosen)
            else:
                await message.channel.send(embed=chosen)
        

def setup(bot):
    bot.add_cog(Fap(bot))