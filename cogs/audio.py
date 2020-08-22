import random
import discord
from discord.ext import commands
from discord.utils import get
import os
import pyttsx3

engine = pyttsx3.init()
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0'
engine.setProperty('voice', voice_id)

class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help="Text to speech. Write something, then the bot joins the voice channel and says it in portuguese")
    async def tts(self, ctx, *, text):
        guild = str(ctx.message.guild.id)
        audio = os.path.isfile("audio/tts"+guild+".mp3")

        try:
            if audio:
                os.remove("audio/tts"+guild+".mp3")
                print("Removed old tts file")
        except PermissionError:
            print("Trying to delete file but audio is being played")
            await ctx.send("ERROR: Audio playing")
            return

        engine.save_to_file(text, "audio/tts"+guild+".mp3")
        engine.runAndWait()

        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        voice.play(discord.FFmpegPCMAudio("audio/tts"+guild+".mp3"), after=lambda e: print("TTS done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volumen = 0.1

    @commands.command(pass_context=True, help="Leaves a voice channel")
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            print(f'The bot has left {channel}')
            message = discord.Embed(description=f"Left {channel} voice channel")
            await ctx.send('', embed=message)
        else:
            print('Bot was told to leave voice channel, but was not in one')
            message = discord.Embed(description=f"Bot is currently not in a voice channel!")
            await ctx.send('', embed=message)

def setup(client):
    client.add_cog(Audio(client))
