import os
import discord
from discord import Embed, Colour
from dotenv import load_dotenv
from vendorsearch import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.bot:
        return

    if message.content.lower().startswith('!vs') and message.author.id == 155821505685487627:  # me only right now
        if not Connected():
            await message.channel.send(f"{message.author.mention} bot is not connected to UO at the moment...")
            return

        await message.channel.send(f"{message.author.mention} searching...")
        _vs = VendorSearch()

        if not _vs.DiscordSearch(message.content.lower()[3:]):
            await message.channel.send(f"{message.author.mention} search either timed out or no items found.")
            return

        if _vs.Results() == 0:
            await message.channel.send(f"{message.author.mention} no results found")
        else:
            _response = f"{message.author.mention} Results Found: {len(_vs.Results())}" \
                        f" currently only supports up to 5"
            await message.channel.send(_response)
            for _result in _vs.Results():
                _color = 'ff7324'
                if _result[0] == 'ring' or _result[0] == 'bracelet':
                    _color = '00ffff'
                _embed = Embed(
                    title=_result[0],
                    colour=Colour(value=int(_color, 16))
                )
                _alt = f'```\n'
                _alt += f'{_result[0]}\n'
                for _i in range(1, len(_result)):
                    _string = _result[_i].split(' ')
                    _value = _string[len(_string) - 1].strip()
                    _name = _result[_i].replace(_value, '').strip().replace(':', '')
                    if _value == 'Antique':
                        _value = 'True'
                        _name = 'Antique'
                    if _string[0] == 'durability':
                        _name = 'durability'
                        _value = _result[_i].replace('durability', '').strip()
                    if _value == 'stone':
                        _name = 'Weight'
                        _value = _result[_i].replace('Weight: ', '').strip()
                    _embed.add_field(name=_name, value=_value)
                    _alt += f'{_name}: {_value}\n'
                # await message.channel.send(embed=_embed)
                _alt += '```'
                await message.channel.send(_alt)
                Wait(1500)

client.run(TOKEN)
