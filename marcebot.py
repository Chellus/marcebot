import discord
import os
from discord.ext import commands
from discord.utils import get
import random

initial_extensions = ['cogs.help']

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('test'))

#gets the client latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ({round(client.latency * 1000)}ms)')

#8ball command
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes - definetly',
    'You may relay on it.',
    'As i see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Do not count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def roll(ctx):
    num = random.randint(1, 100)
    await ctx.send(f'{num}')

@client.command(pass_context=True)
async def play(ctx, *, content=None):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'The bot has left {channel}')
        await ctx.send(f'Left {channel}')
    else:
        print('Bot was told to leave voice channel, but was not in one')
        await ctx.send('Bot is currently not in a voice channel!')

@client.command(pass_context=True)
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
    voice.source.volume = 0.07

@client.command(pass_context=True)
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
    voice.source.volume = 0.07

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{user} has been kicked succesfully.')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f'{user} has been banned succesfully.')
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans() #tuple of users that are banned in the server
    member_name, member_discriminator = member.split('#') #here we split the string into the member name and its
    #discriminator

    for ban_entry in banned_users: #for every banned user in banned users
        user = ban_entry.user

        #if the banned user is the same user as the argument passed to the function, unban this user
        if (user.name, user.discriminator == member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')

#run the bot
client.run('NzQwNzE5ODUzMDIyODcxNjMz.XytHHg.-TYBXPwp2ixH5ljHlrdzKs2CScQ')
