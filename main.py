import asyncio
import discord
from discord import Embed, Colour
from vendorsearch import *

TOKEN = 'DISCORD TOKEN HERE'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

Searches = asyncio.Queue()
RunNextSearch = asyncio.Event()
SearchLock = asyncio.Lock()


async def VendorSearchTask():
    while True:
        RunNextSearch.clear()
        _current = await Searches.get()
        _current.start()
        await RunNextSearch.wait()


async def RunSearch(_message):
    async with SearchLock:
        await _message.channel.send(f"{_message.author.mention} searching...")
        _vs = VendorSearch()

        if not _vs.DiscordSearch(_message.content.lower()[3:]):
            await _message.channel.send(f"{_message.author.mention} search either timed out or no items found.")
            return

        _results = _vs.Results()
        if _results == 0:
            await _message.channel.send(f"{_message.author.mention} no results found")
            return
        else:
            _response = f"{_message.author.mention} Results Found: {len(_results)}"
            await _message.channel.send(_response)
            for _result in _results:
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
                await _message.channel.send(_alt)
                Wait(1500)
    return


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.bot:
        return

    if message.content.lower().startswith('!help'):
        _response = f"```\n" \
                    "HELP MENU\n" \
                    f"usage: !vs param seperated by commas\n" \
                    f"example: !vs dci:15, hci:15, ep:25, antique:true\n" \
                    f"\n" \
                    f"params: di, dci, hci, ssi\n" \
                    f"params: sdi, cf, fcr, fc, lmc, lrc, mw\n" \
                    f"params: garg, elf, cursed, brittle, antique\n" \
                    f"params:ep, luck, rpd, selfrepair, rarity\n" \
                    f"params: physdmg, fdmg, cdmg, pdmg, edmg\n" \
                    f"params: splinter, sort (high/low)```"
        await message.channel.send(_response)

    if message.content.lower().startswith('!vs'):
        if not Connected():  # check if connected to game client
            await message.channel.send(f"{message.author.mention} bot is not connected to UO at the moment...")
            return
        else:
            _search = await RunSearch(message)
            await Searches.put(_search)

#  client.loop.create_task(VendorSearchTask())

client.run(TOKEN)
