import discord
import asyncio

from config import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('cat'):
        await client.send_message(message.channel, 'meow meow')

client.run(TOKEN)
