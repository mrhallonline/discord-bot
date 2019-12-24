import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
token = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix= '.')


@client.event
async def on_ready():
    print(f'{client.user} is connected to Discord')

client.run(token)


