import discord
import os
import json
from discord.ext import commands
from discord.utils import get
import random

with open('facts.json', 'r', encoding="utf8") as data:
    facts = json.load(data)

initial_extensions = ['cogs.help', 'cogs.utility', 'cogs.games']

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('$help'))

@client.command(aliases=['fact'],help="Sends a random fact")
async def randomfact(ctx):
    num = random.randint(1, 50)

    embed = discord.Embed(title="Random fact number "+str(num)+".",
    description=facts[str(num)])

    await ctx.send('', embed=embed)

@client.command(pass_context=True, help="Leaves a voice channel")
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'The bot has left {channel}')
        message = discord.Embed(description=f"Left {channel} voice channel")
        await ctx.send('', embed=message)
    else:
        print('Bot was told to leave voice channel, but was not in one')
        message = discord.Embed(description=f"Bot is currently not in a voice channel!")
        await ctx.send('', embed=message)

@client.command(pass_context=True, help="Plays a random audio related to atucasa")
async def atucasa(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    num = random.randint(1, 2)

    voice.play(discord.FFmpegPCMAudio("audio/atucasa"+str(num)+".mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.1

@client.command(pass_context=True, help="Plays a random audio related to humildad")
async def humildad(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    num = random.randint(1, 3)

    voice.play(discord.FFmpegPCMAudio("audio/humildad"+str(num)+".mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.1

#run the bot
client.run('NzQwNzE5ODUzMDIyODcxNjMz.XytHHg.-TYBXPwp2ixH5ljHlrdzKs2CScQ')
