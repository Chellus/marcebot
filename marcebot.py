import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ({round(client.latency * 1000)}ms)')

@client.command(aliases=['8ball']):
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

client.run('NzQwNzE5ODUzMDIyODcxNjMz.XytHHg.vRsC3n-f966rGwisAYrwADz4OYE')
