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
    content = message.content
    if (' cat ' in content or ' cats ' in content
            or content.startswith('cat ') or content.startswith('cats ')
            or content.endswith(' cat') or content.endswith(' cats')):
        await client.send_message(message.channel, 'meow meow')

client.run(TOKEN)
