import discord
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d? ")

@client.command(pass_context=True)
async def hi(ctx):
    await client.say('Hello <@%s>' % (ctx.message.author.id))




client.run(os.getenv('TOKEN'))


