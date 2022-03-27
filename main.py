import random

import discord
from discord.ext import commands
import scripts
import os

intents = discord.Intents.default()
intents.members= True

bot = commands.Bot(command_prefix='.',
                   case_insensitive=True,
                   description="UWU",
                   strip_after_prefix=True,  # allow "$com" == "$ com"
                   intents=intents
                   )

users=[]
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(pass_context=True)
async def commands(ctx, arg=None):
    message=scripts.commandlist()
    await ctx.channel.send(message)


@bot.command(pass_context=True)
async def idea(ctx, arg=None):
    dire = scripts.check_user_database(ctx.author.id)
    if len(dire) > 5:
        await ctx.channel.send(dire)
    else:
        check=scripts.idea_checklist(dire)
        await ctx.channel.send(check[0])
        if check[1] == 0:
            message = scripts.construct_message(ctx.author.name, dire)
            await ctx.channel.send(message)


@bot.command(pass_context=True)
async def options(ctx, arg=None):
    dire=scripts.check_user_database(ctx.author.id)
    check = scripts.checklist(dire, arg)
    if check[1] != 0:
        message = check[0]
        await ctx.channel.send(message)
    else:
        message = check[0]
        await ctx.channel.send(message)
        if arg == None:
            li = scripts.get_list("data/"+dire+"/main")
        else:
            li = scripts.get_list("data/"+dire+"/"+arg)
        amount = len(li)
        message = scripts.parse_multiple_into_one(amount, li)
        await ctx.channel.send(message)


@bot.command(pass_context=True)
async def addlist(ctx, arg=None):
    dire = scripts.check_user_database(ctx.author.id)
    message = scripts.add_list(dire, arg)
    await ctx.channel.send(message)


@bot.command(pass_context=True)
async def addentries(ctx, arg1 = None, arg2 = None, arg3 = None):
    dire = scripts.check_user_database(ctx.author.id)
    if arg1 == None:
        await ctx.channel.send("Nie podano mi listy!")
        return
    if arg2 == None:
        await ctx.channel.send("Nie podano mi ile razy dodać wpis!")
        return
    if arg3 == None:
        await ctx.channel.send("Nie podano mi co wpisać!")
        return
    path = "data/" + dire + "/" + arg1+".txt"
    print(path)
    if not os.path.exists(path):
        await ctx.channel.send("Nie ma takiej listy!")
        return
    for i in range(int(arg2)):
        scripts.add_to_list("data/" + dire + "/" + arg1, arg3)
    await ctx.channel.send("Zaktualizowano listę: "+arg1+"!")


@bot.command(pass_context=True)
async def newpointcounter(ctx, arg=None):
    if arg == None:
        message=scripts.new_user_points(ctx.author.name)
    else:
        message=scripts.new_user_points(arg)
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
        guild = ctx.guild
        for i in guild.members:
            users.append(i.name)
        message=" dummy "
        for i in users:
            i=i.replace("'", "")
        print(users)
        for i in users:
            #print(i)
            #print(arg)
            if i == arg:
                message = scripts.get_points(arg)
                #print("ok")
                print(message)
                await ctx.channel.send(message)
                return
            else:
                #print(":<")
                message = "Na serwerze nie znalazłem takiego użytkownika!"
    print(message)
    await ctx.channel.send(message)
@bot.command(pass_context=True)
async def makebase(ctx, arg=None):
    message=scripts.make_user_database(ctx.author.id)
    await ctx.channel.send(message)

with open('token.secret') as f1:
    dsc_token = f1.readline()
f1.close()

bot.run(dsc_token)

