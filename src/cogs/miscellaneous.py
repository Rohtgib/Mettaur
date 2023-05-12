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
        while True:
            user = random.choice(server.members)
            try:
                await server.ban(user, reason="Bad RNG")
                embed = discord.Embed(
                    title=f"User {user} was banned",
                    color=0xF4C448,
                )
                embed.add_field(name="Reason:", value="Bad RNG", inline=True)
                await ctx.send(embed=embed)
                break
            except (discord.HTTPException, discord.Forbidden):
                pass

    @randomban.error
    async def randomban_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def randomkick(self, ctx):
        server = ctx.guild
        while True:
            user = random.choice(server.members)
            try:
                await server.kick(user, reason="Bad RNG")
                embed = discord.Embed(
                    title=f"User {user} was kicked",
                    color=0xF4C448,
                )
                embed.add_field(name="Reason:", value="Bad RNG", inline=True)
                await ctx.send(embed=embed)
                break
            except (discord.HTTPException, discord.Forbidden):
                pass

    @randomkick.error
    async def randomkick_error(self, ctx, error):
        await injected(ctx, error)


async def setup(bot):
    await bot.add_cog(miscellaneousCog(bot))
