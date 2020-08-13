import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='Sends the latency of the client.', pass_context=True)
    async def ping(self, ctx):
        await ctx.send('', embed=discord.Embed(description=f'Pong! Latency: {round(self.client.latency * 1000)}ms'))

    @commands.command(help="Kicks a specific member for an optional reason. It takes two parameters. A server member and an optional reason.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send('', embed=discord.Embed(description=f'{user} has been kicked succesfully.'))

    @commands.command(help="Bans a specific member for an optional reason. It takes two parameters. A server member and an optional reason.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send('',embed=discord.Embed(description=f'{user} has been banned succesfully.'))

    @commands.command(help="Unban a banned member from the server. It receives a discord user as an input with its discriminator. User#1234")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans() #every banned user in the server
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (member_name, member_discriminator == user.name, user.discriminator):
                await ctx.guild.unban(user)
                await ctx.send('', embed=discord.Embed(description=f'Unbanned user {user.name}#{user.discriminator}'))

def setup(client):
    client.add_cog(Utility(client))
