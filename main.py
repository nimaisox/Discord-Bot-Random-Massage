import os
import discord
import requests
import random
from keep_alive import keep_alive
from discord.ext import commands


TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix="m")
bot.remove_command('help')

# Presence
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.watching, name =f"نیما فور اور"))
  print(f'Loggin Dis Bot {bot.user}')

snima = ['به به چه  زندگی','نیما عشق است','نیما فور اور.','از بس گاوری. 🤢','خوب میمیبنم که زیاد حرف میزنی! 🐕']

@bot.command()
async def ping(ctx): 
  await ctx.channel.send('ride....')

@bot.command()
async def nima(ctx):
    await ctx.channel.send(random.choice(snima))
    
keep_alive()
bot.run(TOKEN)