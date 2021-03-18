import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("help"):
        
        if str(message.author) == "Morronrost#7833":
            await message.channel.send("Hello " + "@" + str(message.author) + "!")
        else:
            await message.channel.send("testing lol")


client.run(os.getenv('TOKEN'))