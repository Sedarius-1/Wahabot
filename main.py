import random

import discord
from discord.ext import commands
import scripts
bot = commands.Bot(command_prefix='.',
                   case_insensitive=True,
                   description="UWU",
                   strip_after_prefix=True,  # allow "$com" == "$ com"
                   )


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(pass_context=True)
async def idea(ctx, arg=None):
    message = scripts.construct_message(ctx.author.name)
    await ctx.channel.send(message)

@bot.command(pass_context=True)
async def options(ctx, arg=None):
    if arg == None:
        li = scripts.get_list("czynnosci")
    else:
        li = scripts.get_list(arg)
    amount = len(li)
    message = scripts.parse_multiple_into_one(amount, li)
    await ctx.channel.send(message)


@bot.command(pass_context=True)
async def addpoint(ctx, arg=None):
    if arg == None:
        scripts.adding_points(ctx.author.name)
    else:
        scripts.adding_points(arg)
    await ctx.channel.send("Point added! Great job!")


@bot.command(pass_context=True)
async def getpoints(ctx, arg=None):
    if arg == None:
        message=scripts.get_points(ctx.author.name)
    else:
        message=scripts.get_points(arg)
    await ctx.channel.send(message)

with open('token.secret') as f1:
    dsc_token = f1.readline()
f1.close()

bot.run(dsc_token)

# TODO:
# -tak/nie                          $decide
# -wysyłanie sprawozdań             $givspraw <nr_zadania>
# -wtrącanie się do rozmów o nim    "smoli"
# -włamy na głosowy  earrape        "SMOLINUS"
# -cleverbot?                       $converse
