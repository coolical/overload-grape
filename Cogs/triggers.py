import discord, random, asyncio, random
from discord.ext import commands as client
from Cogs.config import conf
discordPlaylistEmbed= discord.Embed(title="Discord Playlist", color=conf.color)
discordPlaylistEmbed.add_field(name="Youtube Playlist: ", value="https://www.youtube.com/playlist?list=PLZCHV2UiCyWrc-bEgcsYLTP2sFd-w0C2p")
discordPlaylistEmbed.add_field(name="Spotify Playlist: ", value="https://open.spotify.com/user/coolical/playlist/3d4iTU9IygolOxnQjjtwLE?si=HUCWDXQnTx-XAhu-uTdc4Q")
discordPlaylistEmbed.add_field(name="Submission Form: ", value="https://goo.gl/forms/SBzO6tlR99fzPBJb2")
discordPlaylistEmbed.add_field(name="Results: ", value="https://docs.google.com/spreadsheets/d/1yprWT1_eihGmfkwLQKFXztQ7yrF-UXYS5vmHjFyEypw/edit?usp=sharing")
triggers = [{"name":"discord playlist", "reply": [discordPlaylistEmbed], "description": "Displays information related to discord playlist", "typeWait": False, "prob": 100},
 {"name":"morning", "reply": ["Good morning! Anyone up for a morning putt?"], "description": "I'll sometimes reply to a morning greeting", "typeWait": True, "prob": 50}]#prob must be [0,100] 
for trigger in triggers:
    try:
        conf.triggers.append({"key":trigger["name"], "value":trigger["description"]})
    except:
        pass

class Triggers(client.Cog):
    def __init__(self, bot):
        self.b = bot

    @client.Cog.listener()
    async def on_message(self, message):
        for trigger in triggers:
            if trigger['name'] in message.content.lower() and not message.author.bot and  random.randint(0,100) <= trigger["prob"]:#checks if bot and if trigger is said and if it can be said based on given probability
                if trigger['typeWait'] == True:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                chosen = random.choice(trigger['reply'])
                if isinstance(chosen, str):#sends choice as repective type
                    await message.channel.send(chosen)
                else:
                    await message.channel.send(embed=chosen)

def setup(bot):
    bot.add_cog(Triggers(bot))