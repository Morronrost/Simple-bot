import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def hello(ctx, *args):
    for arg in args:
        await ctx.send(arg)




client.run(os.getenv('TOKEN'))