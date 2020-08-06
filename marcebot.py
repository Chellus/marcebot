import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
client.run('NzQwNzE5ODUzMDIyODcxNjMz.XytHHg.vRsC3n-f966rGwisAYrwADz4OYE')
