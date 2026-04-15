from dotenv import load_dotenv
import os
import disnake
from disnake.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix=["!", ".", "дэй "], intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} в онлайне")

@bot.command()
async def привет(ctx):
    await ctx.send(f"{ctx.author.mention} 👋")

bot.run(os.getenv("TOKEN"))