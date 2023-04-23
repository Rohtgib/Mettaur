import asyncio
import discord
import os
from discord.ext import commands
from config import Config

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), token=Config.getToken())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

async def setup():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with bot:
        await setup()
        await bot.start(Config.getToken())

asyncio.run(main())