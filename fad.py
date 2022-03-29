import os


def make_user_database(p):
    path = (str(p)[:5])
    print(path)
    is_exist = os.path.exists("data/"+path)
    print(is_exist)
    if is_exist:
        message = "Masz już swoją bazę, nie mogę utworzyć drugiej!"
    if not is_exist:
        os.makedirs("data/"+path)
        message = "Utworzyłem dla Ciebie własną bazę - możesz tworzyć już swoje listy!"
    return message


def check_user_database(p):
    path = (str(p)[:5])
    is_exist = os.path.exists("data/" + path)
    if not is_exist:
        message = "Nie widzę Twojej bazy - przed działaniem musisz ją utworzyć komendą .makebase"
        return message
    if is_exist:
        return path


def checklist(dire, p):
    if p is None:
        p = 'main'
    is_exist = os.path.exists("data/"+dire+'/'+p+'.txt')
    if not is_exist:
        message = "Nie ma takiej listy - musisz ją utworzyć komendą .makelist"
        code = 1
    if is_exist:
        message = "Widzę taką listę - zabieram się do działania!"
        code = 0
    return [message, code]


def add_list(dire, p):
    a = checklist(dire, p)[1]
    if a == 0:
        message = "Taka lista już istnieje - nadpisz ją używając odpowiedniej komendy!"
        return message
    else:
        print("Type of dire:"+str(type(dire)))
        print("Type of p:" + str(type(p)))
        if p is None:
            p = "main"
        with open("data/"+dire+"/"+p+'.txt', 'a') as f1:
            f1.write('p')
        f1.close()
        message = "Nie znalazłem takiej listy więc już ją tworzę!"
        with open("data/"+dire+"/main.txt", 'a') as f2:
            if p == "main":
                f2.write("p" + '\n')
            else:
                f2.write(p+'\n')
        f2.close()
        return message


def remove_list(dire, p):
    if p is None:
        message = "Nie podano mi którą listę usunąć!"
        return message
    a = checklist(dire, p)[1]
    if a == 0:
        os.remove("data/"+dire+"/"+p+'.txt')
        message = "Usunąłem listę "+p+"!"
    else:
        message = "Nie ma takiej listy!"
    return message


def get_list(name):
    with open(name + '.txt') as f1:
        lines1 = f1.readlines()
    f1.close()
    return lines1


def parse_multiple_into_one(amount, li):
    onemes = "List:\n"
    for i in range(amount):
        if i > 9:
            onemes += (str(i + 1) + ". " + li[i])
        else:
            onemes += (str(i + 1) + ".  " + li[i])
    return onemes


def add_to_list(name, addon):
    with open(name + '.txt') as f1:
        lines1 = f1.readlines()
    f1.close()
    if lines1[0] == "p":
        with open(name + '.txt', 'w') as f1:
            f1.write(addon+'\n')
        f1.close()
    else:
        with open(name + '.txt', 'a') as f1:
            f1.write(addon+'\n')
        f1.close()


def remove_from_list(name, line):
    with open(name + '.txt') as f1:
        lines1 = f1.readlines()
        print(len(lines1))
    f1.close()
    with open(name + '.txt', 'w') as f2:
        for index, title in enumerate(lines1, start=1):
            if index != int(line):
                f2.write(title)
    f2.close()
