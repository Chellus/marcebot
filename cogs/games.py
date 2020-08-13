import discord
import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'], help="The user asks a yes–no question to the ball and it replies to it")
    async def _8ball(self, ctx, *, question):
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
        await ctx.send('', embed=discord.Embed(description=f'Question: {question}\nAnswer: {random.choice(responses)}'))

    @commands.command(help='Rolls a random number between 1 and 100')
    async def roll(self, ctx):
        num = random.randint(1, 100)
        message = discord.Embed(description=f"Rolled {num}!")
        await ctx.send('', embed=message)

    @commands.command(help='Flips a coin')
    async def coinflip(self, ctx):
        num = random.randint(1, 2)
        if num == 1:
            await ctx.send('', embed=discord.Embed(description="Tails"))
        else:
            await ctx.send('', embed=discord.Embed(description="Heads"))

def setup(client):
    client.add_cog(Games(client))
