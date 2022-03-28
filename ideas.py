import random
import os


def idea_checklist(path):
    p1 = 'data/'+path+'/main.txt'
    print(p1)
    is_exist1 = os.path.exists('data/'+path+'/main.txt')
    if not is_exist1:
        message = "Nie ma pliku nazwanego main - nie mogę losować! :("
        code = 1
        return [message, code]
    for filename in os.listdir("data/"+path+"/"):
        if filename != 'main.txt':
            message = "Pliki na miejscu - zabieram się do losowania! :)"
            code = 0
            return [message, code]
    message = "Nie ma pliku nienazwanego main - nie mogę losować! :("
    code = 1
    return [message, code]


def activchoice(p, dire):
    with open("data/"+dire+'/'+p + '.txt') as f1:
        lines1 = f1.readlines()
    f1.close()
    z = len(lines1) - 1
    if z < 0:
        z = 0
    n: int = random.randint(0, z)
    print("index:"+str(n))
    print("wylosowane:"+str(lines1[n]))
    nazwa = lines1[n].strip()
    linie = n
    return [nazwa, linie]


def emptycheck(dire):
    l1 = activchoice("main", dire)
    l2 = activchoice(l1[0], dire)
    print("l2[0]:"+l2[0])
    if l2[0] == 'p':
        code = 1
    else:
        code = 0
    print(code)
    return [l1, l2, code]


def construct_message(name, dire):

    lista = emptycheck(dire)
    while lista[2] != 0:
        lista = emptycheck(dire)
    p = "Plan na dziś dla " + name + " - "
    constructed_message = p + lista[0][0] + ": " + lista[1][0]
    return constructed_message
