import os
import discord
from errors import injected
from discord.ext import commands
from config import Config

path = __file__
filename = os.path.basename(path)


class moderationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{filename[:-3].capitalize()} cog loaded")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def wipe(self, ctx, count: int = None):
        if count == None:
            embed = discord.Embed(
                title=f"{Config.getPrefix()}wipe command",
                description="Deletes the given number of messages in a channel",
                color=0xF4C448,
            )
            embed.add_field(
                name="Parameters:", value="(Number of messages, 250 max)", inline=True
            )
            embed.add_field(
                name="Example:", value=f"{Config.getPrefix()}wipe 20", inline=True
            )
            await ctx.send(embed=embed)
        else:
            if count < 1:
                embed = discord.Embed(color=0xFF4A4A)
                embed.add_field(
                    name="Invalid message count provided",
                    value="Make sure the amount of messages you're trying to delete is a number bigger than 0",
                    inline=True,
                )
                await ctx.send(embed=embed)
            elif count > 250:
                await ctx.channel.purge(limit=251)
            else:
                await ctx.channel.purge(limit=count + 1)

    @wipe.error
    async def wipe_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member = None, *, reason="No reason given"):
        if user == None:
            embed = discord.Embed(
                title=f"{Config.getPrefix()}kick command",
                description="Kicks an user from the server",
                color=0xF4C448,
            )
            embed.add_field(
                name="Parameters:", value="(User) (Reason, optional)", inline=True
            )
            embed.add_field(
                name="Example:",
                value=f"{Config.getPrefix()}kick @Rohtgib#5495 stupid",
                inline=True,
            )
            await ctx.send(embed=embed)
        else:
            try:
                await ctx.guild.kick(user, reason=reason)
                embed = discord.Embed(
                    title=f"User {user} was kicked",
                    color=0xF4C448,
                )
                embed.add_field(name="Reason:", value=f"{reason}", inline=True)
                await ctx.send(embed=embed)
            except (discord.HTTPException, discord.Forbidden):
                embed = discord.Embed(color=0xFF4A4A)
                embed.add_field(
                    name="Kick failed",
                    value=f"I couldn't kick user {user}, make sure I have the necessary permissions to kick this user",
                    inline=True,
                )
                await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None, *, reason="No reason given"):
        if user == None:
            embed = discord.Embed(
                title=f"{Config.getPrefix()}ban command",
                description="Bans an user from the server",
                color=0xF4C448,
            )
            embed.add_field(
                name="Parameters:", value="(User) (Reason, optional)", inline=True
            )
            embed.add_field(
                name="Example:",
                value=f"{Config.getPrefix()}ban @Rohtgib#5495 dumb",
                inline=True,
            )
            await ctx.send(embed=embed)
        else:
            try:
                await ctx.guild.ban(user, reason=reason)
                embed = discord.Embed(
                    title=f"User {user} was banned",
                    color=0xF4C448,
                )
                embed.add_field(name="Reason:", value=f"{reason}", inline=True)
                await ctx.send(embed=embed)
            except (discord.HTTPException, discord.Forbidden):
                embed = discord.Embed(color=0xFF4A4A)
                embed.add_field(
                    name="Ban failed",
                    value=f"I couldn't ban user {user}, make sure I have the necessary permissions",
                    inline=True,
                )
                await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int = None, *, reason="No reason given"):
        if user_id == None:
            embed = discord.Embed(
                title=f"{Config.getPrefix()}uban command",
                description="Unbans an user from the server",
                color=0xF4C448,
            )
            embed.add_field(
                name="Parameters:", value="(User ID) (Reason: Optional)", inline=True
            )
            embed.add_field(
                name="Example:",
                value=f"{Config.getPrefix()}unban @Rohtgib#5495",
                inline=True,
            )
            await ctx.send(embed=embed)
        else:
            try:
                user = await self.bot.fetch_user(user_id)
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title=f"User {user} has been ubanned",
                    color=0xF4C448,
                )
                embed.add_field(name="Reason:", value=f"{reason}", inline=True)
                await ctx.send(embed=embed)
            except (discord.HTTPException, discord.Forbidden):
                embed = discord.Embed(color=0xFF4A4A)
                embed.add_field(
                    name="Unban failed",
                    value=f"I couldn't unban user {user}, are you sure they're even banned?",
                    inline=True,
                )
                await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        await injected(ctx, error)


async def setup(bot):
    await bot.add_cog(moderationCog(bot))
