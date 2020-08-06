import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *cog):
        #Gets all cogs and commands of mine.
        try:
            if not cog:
                #Cog listing
                halp = discord.Embed(title='Cog listing and Uncategorized commands',
                description='Use `$help *cog*` to find out more about them!\n(BTW, the Cog Name Must Be in Title Case, Just Like This Sentence.)')
                cogs_desc = ''
                for x in self.client.cogs:
                    cogs_desc += ('{} - {}'.format(x, self.client.cogs[x].__doc__)+'\n')
                halp.add_field(name='Cogs', value=cogs_desc[0:len(cogs_desc)-1],inline=False)
                cmd_desc = ''
                for y in self.client.walk_commands():
                    if not y.cog_name and not y.hidden:
                        cmd_desc += ('{} - {}'.format(y.name,y.help)+'\n')
                halp.add_field(name='Uncatergorized Commands',value=cmds_desc[0:len(cmds_desc)-1],inline=False)
                await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('',embed=halp)

            else:
                #Helps me remind you if you pass too many args
                if len(cog) > 1:
                    halp = discord.Embed(title='Error!',description='That is way too many cogs!',color=discord.Color.red())
                    await ctx.message.author.send('',embed=halp)
                else:
                    #Command listing within a cog
                    found = False
                    for x in self.client.cogs:
                        for y in cog:
                            if x == y:
                                halp=discord.Embed(title=cog[0]+' Command Listing',description=self.client.cogs[cog[0]].__doc__)
                                for c in self.client.get_cog(y).get_commands():
                                    if not c.hidden:
                                        halp.add_field(name=c.name,value=c.help,inline=False)
                                found = True
                    if not found:
                        #Reminds you if that cog doesn't exist
                        halp = discord.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=discord.Color.red())
                    else:
                        await ctx.message.add_reaction(emoji='✉')
                    await ctx.message.author.send('',embed=halp)
        except:
            await ctx.send("Excuse me, I can't send embeds.")

def setup(client):
    client.add_cog(HelpCog(client))
