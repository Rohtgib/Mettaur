import os
import discord
from discord.ext import commands

path = __file__
filename = os.path.basename(path)


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{filename} loaded')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def wipe(self, ctx, count=None):
        if count == None:
            embed = discord.Embed(
                title="m!wipe command", description="Deletes the given number of messages in a channel", color=0xf4c448)
            embed.add_field(name="Parameters:",
                            value="Number of messages (250 max)", inline=True)
            embed.add_field(name="Example:",
                            value="m!wipe 20", inline=True)
            await ctx.send(embed=embed)
        else:
            try:
                count = int(count)
                if count < 1:
                    embed = discord.Embed(color=0xff4a4a)
                    embed.add_field(name="Error: Invalid message count provided",
                                    value="Make sure the amount of messages you're trying to delete is a number bigger than 0", inline=True)
                    await ctx.send(embed=embed)
                elif count > 250:
                    await ctx.channel.purge(limit=int(251))
                else:
                    await ctx.channel.purge(limit=int(count+1))
            except ValueError:
                embed = discord.Embed(color=0xff4a4a)
                embed.add_field(name="Error: Invalid message count provided",
                                value="Make sure the amount of messages you're trying to delete is a actually number", inline=True)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, *, reason="No reason given"):
        pass

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, user: discord.Member, *, reason="No reason given"):
        pass

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, user: int, *, reason="No reason given"):
        pass


async def setup(bot):
    await bot.add_cog(Moderation(bot))
