
import discord
from discord.ext import commands
import fad
import calc
import ideas
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.',
                   case_insensitive=True,
                   description="UWU",
                   strip_after_prefix=True,
                   intents=intents
                   )

users = []


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(pass_context=True)
async def commands(ctx):
    message = calc.commandlist()
    await ctx.channel.send(message)


@bot.command(pass_context=True)
async def make_base(ctx, arg=None):
    message = fad.make_user_database(ctx.author.id)
    dire = fad.check_user_database(ctx.author.id)
    fad.add_list(dire, arg)
    await ctx.channel.send(message)


@bot.command(pass_context=True)
async def idea(ctx):
    dire = fad.check_user_database(ctx.author.id)
    if len(dire) > 5:
        await ctx.channel.send(dire)
    else:
        check = ideas.idea_checklist(dire)
        await ctx.channel.send(check[0])
        if check[1] == 0:
            message = ideas.construct_message(ctx.author.name, dire)
            await ctx.channel.send(message)


@bot.command(pass_context=True)
async def show_list(ctx, arg=None):
    dire = fad.check_user_database(ctx.author.id)
    check = fad.checklist(dire, arg)
    if check[1] != 0:
        message = check[0]
        await ctx.channel.send(message)
    else:
        message = check[0]
        await ctx.channel.send(message)
        if arg is None:
            li = fad.get_list("data/"+dire+"/main")
        else:
            li = fad.get_list("data/"+dire+"/"+arg)
        amount = len(li)
        message = fad.parse_multiple_into_one(amount, li)
        await ctx.channel.send(message)


@bot.command(pass_context=True)
async def add_list(ctx, arg=None):
    dire = fad.check_user_database(ctx.author.id)
    message = fad.add_list(dire, arg)
    await ctx.channel.send(message)


@bot.command(pass_context=True)
async def add_ent(ctx, arg1=None, arg2=None, arg3=None):
    dire = fad.check_user_database(ctx.author.id)
    if arg1 is None:
        await ctx.channel.send("Nie podano mi listy!")
        return
    if arg2 is None:
        await ctx.channel.send("Nie podano mi ile razy dodać wpis!")
        return
    if arg3 is None:
        await ctx.channel.send("Nie podano mi co wpisać!")
        return
    path = "data/" + dire + "/" + arg1+".txt"
    print(path)
    if not os.path.exists(path):
        await ctx.channel.send("Nie ma takiej listy!")
        return
    for i in range(int(arg2)):
        fad.add_to_list("data/" + dire + "/" + arg1, arg3)
    await ctx.channel.send("Zaktualizowano listę: "+arg1+"!")


@bot.command(pass_context=True)
async def rem_ent(ctx, arg1=None, arg2=None):
    dire = fad.check_user_database(ctx.author.id)
    if arg1 is None:
        await ctx.channel.send("Nie podano mi listy!")
        return
    if arg2 is None:
        await ctx.channel.send("Nie podano mi którą linię usunąć!")
        return
    path = "data/" + dire + "/" + arg1 + ".txt"
    if not os.path.exists(path):
        await ctx.channel.send("Nie ma takiej listy!")
        return
    fad.remove_from_list("data/" + dire + "/" + arg1, arg2)


@bot.command(pass_context=True)
async def new_p_count(ctx, arg=None):
    if arg is None:
        message = calc.new_user_points(ctx.author.name)
    else:
        message = calc.new_user_points(arg)
    await ctx.channel.send(message)


@bot.command(pass_context=True)
async def add_p(ctx, arg=None):
    if arg is None:
        calc.adding_points(ctx.author.name)
    else:
        calc.adding_points(arg)
    await ctx.channel.send("Point added! Great job!")


@bot.command(pass_context=True)
async def get_p(ctx, arg=None):
    if arg is None:
        message = calc.get_points(ctx.author.name)
    else:
        guild = ctx.guild
        for i in guild.members:
            users.append(i.name)
        message = " dummy "
        for i in users:
            i.replace("'", "")
        print(users)
        for i in users:
            if i == arg:
                message = calc.get_points(arg)
                await ctx.channel.send(message)
                return
            else:
                message = "Na serwerze nie znalazłem takiego użytkownika!"
    print(message)
    await ctx.channel.send(message)


with open('token.secret') as f1:
    dsc_token = f1.readline()
f1.close()

bot.run(dsc_token)
