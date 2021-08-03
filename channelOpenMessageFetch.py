import discord
from discord.ext import commands
def fetchChannelMessages(channel, client):
    return channel.history(limit=40)