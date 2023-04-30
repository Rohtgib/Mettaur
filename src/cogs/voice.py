import os
import discord
import datetime
from errors import injected
from discord.ext import commands
from config import Config

path = __file__
filename = os.path.basename(path)


class voiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{filename[:-3].capitalize()} cog loaded")

    @commands.command()
    async def join(self, ctx):
        if not ctx.author.voice:
            await ctx.send("Make sure you're in a voice channel first")
            return
        await ctx.author.voice.channel.connect()

    @join.error
    async def join_error(self, ctx, error):
        await injected(self, error)

    @commands.command()
    async def leave(self, ctx):
        if not ctx.author.voice or not ctx.guild.voice_client:
            await ctx.send("I'm not in a voice channel with you")
            return
        elif ctx.author.voice.channel != ctx.guild.voice_client.channel:
            await ctx.send(
                "You need to be in the same voice channel as me to disconnect me"
            )
            return
        await ctx.guild.voice_client.disconnect()

    @leave.error
    async def leave_error(self, ctx, error):
        await injected(self, error)

    @commands.command()
    async def play(self, ctx):
        if not ctx.author.voice:
            await ctx.send("Make sure you're in a voice channel first")
            return
        elif ctx.author.voice.channel != ctx.guild.voice_client.channel:
            await ctx.send("We're not in the same voice channel")
            return
        elif ctx.author.voice and not ctx.guild.voice_client:
            ctx.author.voice.channel.connect()
        # Test with local files instead of URLs, this section is not working
        source = await discord.PCMVolumeTransformer(
            discord.FFmpegOpusAudio.from_probe(
                "https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav"
            )
        )
        await ctx.guild.voice_client.play(
            source, after=lambda e: print("Player error: %s" % e) if e else None
        )
        #


async def setup(bot):
    await bot.add_cog(voiceCog(bot))
