import random
import discord
import os
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
d={}
@bot.event
async def on_ready():
    await bot.change_presence( status = discord.Status.online, activity = discord.Game('Личный клоун Дмитрия'))
@bot.command(pass_context=True)
async def help(ctx):
    emb=discord.Embed(title='Список возможных команд')
    emb.add_field(name = '{}hi'.format('!'), value = 'Поздороваться')
    emb.add_field(name = '{}dicklen'.format('!'), value = 'Измерить длину вашего прибора')
    emb.add_field(name = '{}clear (введенное число)'.format('!'), value = 'Удалить последние (введенное число) сообщений')
    await ctx.send(embed = emb)
@bot.command(pass_context=True)ф
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
@bot.command(pass_context=True)
async def clear(ctx, x = 1):
    x=int(x)+1
    await ctx.channel.purge(limit = x)
#bot.run(TOKEN)
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
