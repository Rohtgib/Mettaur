import discord
from discord.ext import commands


async def injected(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(color=0xFF4A4A)
        embed.add_field(
            name="User not found",
            value=f"I couldn't find this user, make sure you're using the right user ID or mentioning the user",
            inline=True,
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(color=0xFF4A4A)
        embed.add_field(
            name="Wrong argument used",
            value=f"I couldn't use the argument you passed, make sure it's the right one",
            inline=True,
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(color=0xFF4A4A)
        embed.add_field(
            name="Missing permissions",
            value=f"I don't have the necessary permissions to execute this command",
            inline=True,
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=0xFF4A4A)
        embed.add_field(
            name="Something went wrong",
            value=f"An error ocurred, but I can't exactly tell you why",
            inline=True,
        )
        await ctx.send(embed=embed)
