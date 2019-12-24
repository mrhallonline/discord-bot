import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
token = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix= '.')


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server'
    )

client.run(token)


