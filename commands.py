import discord
import youtube_dl
import os

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.webm")
    try:
        if song_there:
            os.remove("song.webm")
    except PermissionError:
        await ctx.send("Music is already playing.")
        return


    voiceChannel = ctx.message.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
        
    ydl_opts = {
        'format': '249/250/251'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".webm"):
            os.rename(file, "song.webm")
    voice.play(discord.FFmpegOpusAudio("song.webm"))



@client.command()
async def dc(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel. ")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Audio is not paused")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()



client.run(os.getenv('TOKEN'))