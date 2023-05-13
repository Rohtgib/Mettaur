import os
import discord
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
        user = ctx.author
        coin = random.randint(1, 2)
        if coin == 1:
            coin = "Heads"
        else:
            coin = "Tails"
        embed = discord.Embed(title=f"Coin flip by {user.display_name}", color=0xF4C448)
        embed.set_author(name=user, icon_url=user.display_avatar.url)
        embed.add_field(
            name="The coin landed on...",
            value=f":coin: {coin}",
            inline=True,
        )
        await ctx.send(embed=embed)

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    async def roll(self, ctx):
        user = ctx.author
        die = random.randint(1, 6)
        embed = discord.Embed(title=f"Die roll by {user.display_name}", color=0xF4C448)
        embed.set_author(name=user, icon_url=user.display_avatar.url)
        embed.add_field(
            name=f"The die landed on...",
            value=f":game_die: {die}",
            inline=True,
        )
        await ctx.send(embed=embed)

    @roll.error
    async def roll_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    async def rps(self, ctx):
        pass

    @rps.error
    async def rps_error(self, ctx, error):
        await injected(ctx, error)


async def setup(bot):
    await bot.add_cog(gamesCog(bot))
