import os
import discord
import datetime
from errors import injected
from discord.ext import commands
from config import Config
from interfaces.time import datetimeDiscord

path = __file__
filename = os.path.basename(path)


class aboutCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{filename[:-3].capitalize()} cog loaded")

    @commands.command()
    async def server(self, ctx):
        await ctx.send("Information about the server")

    @server.error
    async def command_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    async def who(self, ctx, user: discord.Member = None):
        # Nickname (if there's even one) - display_name
        # Whole username (User#Discrim) - pretty sure just the object
        # Profile picture - display_avatar
        # When did the user make their account - created_at
        # When did the user join the server - joined_at
        # User ID - id
        # User permissions in the server - guild_permissions
        # User roles - roles
        if user == None:
            user = ctx.author
            userCreated = datetimeDiscord(user.created_at)
            userJoined = datetimeDiscord(user.joined_at)
            userRoles = [f"{role.mention}" for role in user.roles if role.name != "@everyone"]
            userPermissions = [perm.replace("_", " ").title() for perm, value in user.guild_permissions]
            embed = discord.Embed(title=user.mention)
            embed.set_author(name=user, icon_url=user.display_avatar.url)
            embed.set_thumbnail(url=user.display_avatar.url)
            embed.add_field(name="Discord member since", value=userCreated.formatted_date, inline=True)
            embed.add_field(name="Server member since", value=userJoined.formatted_date, inline=True)
            embed.add_field(name="Roles", value=' '.join(userRoles), inline=False)
            embed.add_field(name="Permissions", value=', '.join(userPermissions), inline=False)
            embed.set_footer(text=f"ID: {user.id}")
            await ctx.send(embed=embed)
        else:
            userCreated = datetimeDiscord(user.created_at)
            userJoined = datetimeDiscord(user.joined_at)
            userRoles = [f"{role.mention}" for role in user.roles if role.name != "@everyone"]
            userPermissions = [perm.replace("_", " ").title() for perm, value in user.guild_permissions]
            embed = discord.Embed(title=user.mention)
            embed.set_author(name=user, icon_url=user.display_avatar.url)
            embed.set_thumbnail(url=user.display_avatar.url)
            embed.add_field(name="Discord member since", value=userCreated.formatted_date, inline=True)
            embed.add_field(name="Server member since", value=userJoined.formatted_date, inline=True)
            embed.add_field(name="Roles", value=' '.join(userRoles), inline=False)
            embed.add_field(name="Permissions", value=', '.join(userPermissions), inline=False)
            embed.set_footer(text=f"ID: {user.id}")
            await ctx.send(embed=embed)

    @who.error
    async def who_error(self, ctx, error):
        await injected(ctx, error)

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title="About Mettaur",
            description="Mettaur is a multipurpose, self hosted Discord bot",
            color=0xF4C448,
        )
        embed.add_field(
            name="Single server alternative to popular bots",
            value="Mettaur's purpose is serving as a **backup bot** in case other general purpose bots go on an outage",
            inline=True,
        )
        embed.add_field(
            name="Features",
            value=f"General moderation commands, server wide information display, and some other miscellaneous daily use commands most other Discord bots share, if you want to take a look at all the commands run the **{Config.getPrefix()}help** command",
            inline=True,
        )
        embed.add_field(name="Prefix", value=f"{Config.getPrefix()}", inline=True)
        embed.add_field(
            name="Coded and mantained by", value="<@355198184198373409>", inline=True
        )
        embed.add_field(
            name="Our website",
            value="(Website link here, make a website btw lol)",
            inline=True,
        )
        embed.add_field(
            name="Get the latest updates", value="(GitHub link here)", inline=True
        )
        await ctx.send(embed=embed)

    @about.error
    async def about_error(self, ctx, error):
        await injected(ctx, error)


async def setup(bot):
    await bot.add_cog(aboutCog(bot))
