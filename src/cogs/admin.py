import os
import discord
from errors import injected
from discord.ext import commands

path = __file__
filename = os.path.basename(path)

class adminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{filename[:-3].capitalize()} cog loaded')

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.author.id != ctx.guild.owner_id:
            return
        await ctx.send('Shutting down...')
        print("------")
        print("Mettaur is shutting down, thank you for using me!")
        await self.bot.close()
    
    @shutdown.error
    async def shutdown_error(self, ctx, error):
        await injected(ctx, error)

async def setup(bot):
    await bot.add_cog(adminCog(bot))
