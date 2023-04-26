import asyncio
import discord
import os
from discord.ext import commands
from config import Config

bot = commands.Bot(
    command_prefix="m!",
    help_command=None,
    intents=discord.Intents.all(),
    token=Config.getToken(),
)


@bot.event
async def on_ready():
    print(f"Starting up as {bot.user.name} ({bot.user.id})")
    print("------")
    await bot.change_presence(activity=discord.Game(name="Megaman X6"))


async def setup():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await setup()
        await bot.start(Config.getToken())


asyncio.run(main())
