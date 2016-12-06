import logging
import re

import discord
import asyncio

from config import TOKEN


logger = logging.getLogger('catbot')

client = discord.Client()


CANNED_RESPONSES = {
    'kitten': 'mew mew',
    'kittie': 'mew mew',
    'kittez': 'mew mew',
    'kittehz': 'mew mew',
    'kitteh': 'mew mew',
    'kitties': 'mew mew',
    'kitty': 'mew mew',
    'string': 'mew',
    'yarn': 'mew',
    'cream': 'mreow',
    'milk': 'mreow',
    'tuna': 'mreow',
    'fish': 'mreow',
    'prr': 'prrr prrr',
    'purr': 'purrr',
    'cats': 'meow meow',
    'cat' : 'meow',
}


@client.event
async def on_ready():
    print('Logged in as {} ({})'.format(
        client.user.name, client.user.id))

@client.event
async def on_message(message):
    content = message.content
    response = get_response(content)
    if response is not None:
        await client.send_message(message.channel, response)


def get_response(message_content):
    words = re.findall(r"[\w]+", message_content)
    for keyword in CANNED_RESPONSES:
        if keyword in words:
            return CANNED_RESPONSES[keyword]
    return None


if __name__ == '__main__':
    client.run(TOKEN)
