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


async def setup(bot):
    await bot.add_cog(voiceCog(bot))
