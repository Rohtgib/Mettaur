import discord
from discord.ext import commands

async def injected(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(color=0xff4a4a)
        embed.add_field(name="User not found",
                        value=f"I couldn't find this user, make sure you're passing using the right user ID or mentioning the user", inline=True)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(color=0xff4a4a)
        embed.add_field(name="Wrong argument used",
                        value=f"I couldn't use the argument you passed, make sure it's the right one", inline=True)
        await ctx.send(embed=embed)