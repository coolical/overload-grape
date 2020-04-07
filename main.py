import discord, os, traceback, chalk, sys
from discord.ext import commands
from Cogs.config import conf

Cogs = conf.cogd
async def prefix(bot, message):
  return [conf.prefix1, conf.prefix2]  # or a list, ["pre1","pre2"]
client = commands.Bot(command_prefix=prefix, status=discord.Status.idle, activity=discord.Game(name="Starting Up...")) # Defining what our prefix for the bot will be
if __name__=='__main__': #loads every file with .py extension in Cogs folder
    for file in os.listdir(conf.cogd):
        if file.endswith('.py'):
            name=file[:-3]
            if name == 'config':
                pass
            else:
                try:
                    client.load_extension(f'Cogs.{name}')
                    print(chalk.green(f'[INFO] Loaded {name}'))
                except (discord.ClientException, ModuleNotFoundError):
                    print('[ERROR] Failed to load Cog {name}')
                    print(traceback.format_exc())
                    continue
print(os.environ['TOKEN'])
print(str(os.environ['TOKEN']))
print(isinstance(os.environ['TOKEN'], str))
client.run(str(os.environ['TOKEN'])) # replace os.environ['TOKEN'] login via your token
