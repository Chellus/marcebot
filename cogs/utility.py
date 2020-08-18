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

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member')

    @commands.command(help="Bans a specific member for an optional reason. It takes two parameters. A server member and an optional reason.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send('',embed=discord.Embed(description=f'{user} has been banned succesfully.'))

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member')

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

    @commands.command(help="Mutes a member so that he cannot send messages")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, user : discord.Member, *, reason=None):
        try:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await user.add_roles(role)
            await ctx.send(f'I have muted {user.mention} for the reason: {reason}')
        except:
            perms = discord.Permissions(send_messages=False, read_messages=True)

            await ctx.guild.create_role(name="Muted", permissions=perms)
            await user.add_roles(role)
            await ctx.send(f'I have muted {user.mention} for the reason: {reason}')

    @mute.error
    async def mute_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member')

    @commands.command(help="Unmutes a member so that he can send messages again")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, user : discord.Member):
        try:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            if role in user.roles:
                await user.remove_roles(role)
                await ctx.send(f'Unmuted {user.mention}')
            else:
                await ctx.send(f'The user {user.mention} is not muted.')
        except:
            await ctx.send(f'The user {user.mention} is not muted.')

    @unmute.error
    async def unmute_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member')

    @commands.command(aliases=['whois'], help='Get more info about a certain user')
    async def userinfo(self, ctx, member : discord.Member=None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=discord.Colour.green(), timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Guild name:", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles:", value="".join([role.mention for role in roles[1:]]))
        embed.add_field(name="Bot?:", value=member.bot)

        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member')

def setup(client):
    client.add_cog(Utility(client))
