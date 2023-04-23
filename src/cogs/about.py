import os
import discord
from discord.ext import commands

path = __file__
filename = os.path.basename(path)

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{filename} loaded')

    @commands.command()
    async def about(self, ctx):
        await ctx.send("I am Mettaur")


async def setup(bot):
    await bot.add_cog(About(bot))