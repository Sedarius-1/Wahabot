import random

import discord
import scripts
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(Message):
    if Message.author == client.user:
        return
    if ".idea" in Message.content.lower():
            message=scripts.construct_message(Message.author.name)
            await Message.channel.send(message)
        # file = discord.File(r"nocom.gif")
        # await Message.channel.send(file=file, content="Sus")
    if ".options" in Message.content.lower():

        wiad=Message.content.split(" ")
        if len(wiad) == 1:
            li = scripts.get_list("czynnosci")
        else:
            li=scripts.get_list(wiad[1])
        amount = len(li)
        message=scripts.parse_multiple_into_one(amount, li)
        await Message.channel.send(message)
    if ".addpoints" in Message.content.lower():
        scripts.adding_points(Message.author.name)

with open('token.secret') as f1:
    dsc_token = f1.readline()
f1.close()

client.run(dsc_token)

# TODO:
# -tak/nie                          $decide
# -wysyłanie sprawozdań             $givspraw <nr_zadania>
# -wtrącanie się do rozmów o nim    "smoli"
# -włamy na głosowy  earrape        "SMOLINUS"
# -cleverbot?                       $converse
