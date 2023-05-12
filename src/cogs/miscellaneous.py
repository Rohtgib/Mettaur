import os
import discord
import random
from errors import injected
from discord.ext import commands
from config import Config
# from moderation import ban, ban_error, kick, kick_error

path = __file__
filename = os.path.basename(path)


class miscellaneousCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{filename[:-3].capitalize()} cog loaded")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def randomban(self, ctx):
        server = ctx.guild
        user = random.choice(server.members)
        await ctx.send(f"{user} I see you.")
#        await ban(self, ctx, user,"Bad RNG")
    
    @randomban.error
    async def randomban_error(self, ctx, error):
        await injected(ctx,error)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def randomkick(self, ctx):
        server = ctx.guild
        user = random.choice(server.members)
        await ctx.send(f"{user} I see you.")
    
    @randomkick.error
    async def randomkick_error(self, ctx, error):
        await injected(ctx,error)


async def setup(bot):
    await bot.add_cog(miscellaneousCog(bot))
