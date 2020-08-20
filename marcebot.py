import discord
import os
import json
from discord.ext import commands
from discord.utils import get
import random

with open('facts.json', 'r', encoding="utf8") as data:
    facts = json.load(data)

initial_extensions = ['cogs.help', 'cogs.utility', 'cogs.games', 'cogs.audio']

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('$help'))

@client.command(help="Sends a random fact")
async def randomfact(ctx):
    num = random.randint(1, 50)

    embed = discord.Embed(title="Random fact number "+str(num)+".",
    description=facts[str(num)])

    await ctx.send('', embed=embed)

@client.command(help="Look something up on the internet")
async def lmgtfy(ctx, *, search=None): #let me google that for you
    if search == None:
        await ctx.send("I need something to search.")
    else:
        search = search.replace(" ", "+")
        await ctx.send("https://es.lmgtfy.com/?q="+search+"&pp=1&s=l&iie=1")

#run the bot
client.run('NzQwNzE5ODUzMDIyODcxNjMz.XytHHg.-TYBXPwp2ixH5ljHlrdzKs2CScQ')
