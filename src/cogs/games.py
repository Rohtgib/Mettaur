import os
import discord
import datetime
import random
from errors import injected
from discord.ext import commands
from config import Config

path = __file__
filename = os.path.basename(path)


class gamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{filename[:-3].capitalize()} cog loaded")

    @commands.command()
    async def coinflip(self, ctx):
        coin = random.randint(1,2)
        await ctx.send(coin)
        if coin == 1:
            await ctx.send("Coin landed on heads")
        else:
            await ctx.send("Coin landed on tails")

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    async def roll(self, ctx, die: int = 1):
        if die > 2:
            await ctx.send("I'm currently limited to only rolling 2 dice per command")
            return
        while i < die:
            die = random.randint(1,2,3,4,5,6)
        

async def setup(bot):
    await bot.add_cog(gamesCog(bot))
