import random
import discord
import openpyxl
client = discord.Client()


def activchoice(p):
    with open(p + '.txt') as f1:
        lines1 = f1.readlines()
    f1.close()
    n: int = random.randint(0, len(lines1) - 1)
    nazwa = lines1[n].strip()
    linie = n
    print(nazwa, '\n', linie)
    return [nazwa, linie]
    # return lines1[n].strip(), n


def emptycheck():
    p = 0
    while p == 0:
        l1 = activchoice("czynnosci")
        l2 = activchoice(l1[0])
        p = l2[1]
    return [l1, l2]


def construct_message(name):
    lista = emptycheck()
    p = "Plan na dziś dla " + name + " - "
    constructed_message = p + lista[0][0] + ": " + lista[1][0]
    return constructed_message


def get_list(name):
    with open(name + '.txt') as f1:
        lines1 = f1.readlines()
    f1.close()
    return lines1


def parse_multiple_into_one(amount, li):
    onemes = "List:\n"
    for i in range(amount):
        onemes += (str(i + 1) + ". " + li[i])
    return onemes


#def adding_points(p):
    #path = points.xlsx
    #f.close()
