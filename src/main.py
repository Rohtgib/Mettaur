import asyncio
import discord
import os
import logging
from discord.ext import commands
from config import Config

while True:
    debugMode = input("Run in debug mode? Y/N: ")
    if debugMode.upper() == "Y":
        logging.basicConfig(level=logging.DEBUG)
        print("Running in debug mode")
        break
    if debugMode.upper() == "N":
        print("Running on normal mode")
        break
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    clear()


bot = commands.Bot(
    command_prefix=Config.getPrefix(),
    help_command=None,
    intents=discord.Intents.all(),
    token=Config.getToken(),
)


@bot.event
async def on_ready():
    print(f"Starting up as {bot.user.name} ({bot.user.id})")
    print(f"Current prefix is {Config.getPrefix()}")
    print("------")
    await bot.change_presence(activity=discord.Game(name=f"{Config.getStatus()}"))


async def setup():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await setup()
        await bot.start(Config.getToken())


asyncio.run(main())
