import random
import discord
import os
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
d={}
@bot.command(pass_context=True)
async def hi(ctx):
    await ctx.send('Hey, {}'.format(ctx.message.author.mention))
@bot.command(pass_context=True)
async def dicklen(ctx):
    try:
        await ctx.send(d[format(ctx.message.author.id)] + 'cm - is your dick size {}'.format(ctx.message.author.mention))
    except KeyError:
        c={format(ctx.message.author.id): str(random.randrange(10, 31))}
        d.update(c)
        await ctx.send(d[format(ctx.message.author.id)] + 'cm - is your dick size {}'.format(ctx.message.author.mention))
#bot.run(TOKEN)
token = os.environ.get(BOT_TOKEN)
bot.run(str(token))
