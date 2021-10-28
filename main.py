import discord
from discord.ext import commands
import requests
import colorama
import json

with open('config.json', 'r') as f:
    config = json.load(f)


token = config.get('token')
statusname = config.get('statusname')
twitchurl = config.get('twitchurl')

intents=discord.Intents.all()
intents.members = True

solar = commands.Bot(command_prefix='o', self_bot=True, case_insensitive=False,intents=intents)
solar.remove_command('help')

@solar.event
async def on_connect():
  print('''
\033[0;35m╔═╗┌┬┐┬─┐┌─┐┌─┐┌┬┐┬┌┐┌┌─┐\033[0m\
\033[0;90m╚═╗ │ ├┬┘├┤ ├─┤││││││││ ┬\033[0m\
\033[0;37m╚═╝ ┴ ┴└─└─┘┴ ┴┴ ┴┴┘└┘└─┘\033[0m\
  ''')

@solar.event
async def on_ready():
  print("Status Loop Activated")
  while True:
     await solar.change_presence(activity=discord.Streaming (url = twitchurl, name= statusname))

solar.run(token, bot=False)
