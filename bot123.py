import discord
from bot_mantik import gen_pass

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='..', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("hi" * count_heh)
@bot.command()
async def oreo(ctx, count_reo = 10):
    await ctx.send("oreo" * count_heh)

bot.run("token")

