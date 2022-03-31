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
        message = "Nie widzę Twojej bazy - przed działaniem musisz ją utworzyć komendą .make_base"
        return message
    if is_exist:
        return path


def checklist(dire, p):
    if p is None:
        p = 'main'
    print(p.isalnum())
    if p.isalnum() is False:
        message = "Nie ma takiej listy - podano znaki niealfanumeryczne!"
        code = 2
        return [message, code]
    p = p.lower()
    is_exist = os.path.exists("data/"+dire+'/'+p+'.txt')
    if not is_exist:
        message = "Nie ma takiej listy - musisz ją utworzyć komendą .add_list"
        code = 1
    else:
        message = "Widzę taką listę - zabieram się do działania!"
        code = 0
    return [message, code]


def add_list(dire, p):
    a = checklist(dire, p)[1]
    if a == 2:
        message = checklist(dire, p)[0]
        return message
    if a == 0:
        message = "Taka lista już istnieje - nadpisz ją używając odpowiedniej komendy!"
        return message
    else:
        print("Type of dire:"+str(type(dire)))
        print("Type of p:" + str(type(p)))
        if p is None:
            p = "main"
        with open("data/"+dire+"/"+p+'.txt', 'a') as f1:
            f1.write('p\n')
        f1.close()
        with open("data/" + dire + "/main.txt", 'r') as f2:
            line1 = f2.readline()
        f2.close()
        print(line1)
        message = "Nie znalazłem takiej listy więc już ją tworzę!"
        if line1 == 'p\n':
            with open("data/" + dire + "/main.txt", 'w') as f2:
                if p == "main":
                    pass
                else:
                    f2.write(p + '\n')
            f2.close()
        else:
            with open("data/"+dire+"/main.txt", 'a') as f2:
                if p == "main":
                    pass
                else:
                    f2.write(p+'\n')
            f2.close()
        return message


def copy_list(dire, p, c):
    if p is None or c is None:
        message = "Nie podano mi wystarczająco argumentów!"
        return message
    a = checklist(dire, p)[1]
    z = checklist(dire, c)[1]
    if a == 2 or z == 2:
        message = checklist(dire, p)[0]
        return message
    if z == 0:
        message = "Lista podana jako nowa nazwa już istnieje jako lista!"
        return message
    if a == 0:
        with open("data/"+dire+"/"+p+'.txt', 'r') as f1:
            lines1 = f1.readlines()
        f1.close()
        with open("data/"+dire+"/"+c+'.txt', 'a') as f2:
            for i in lines1:
                f2.write(i)
        f2.close()
        message = "Skopiowałem listę "+p+" do "+c+"!"
        return message
    else:
        message = "Nie mogę skopiować listy która nie istnieje!"
        return message


def remove_list(dire, p):
    if p is None:
        message = "Nie podano mi którą listę usunąć!"
        return message
    a = checklist(dire, p)[1]
    if a == 2:
        message = checklist(dire, p)[0]
        return message
    if a == 0:
        os.remove("data/"+dire+"/"+p+'.txt')
        message = "Usunąłem listę "+p+"!"
        with open("data/" + dire + "/main.txt", 'r') as f1:
            lines1 = f1.readlines()
        f1.close()
        with open("data/" + dire + "/main.txt", 'w') as f2:
            for index, title in enumerate(lines1, start=1):
                if title != p+"\n":
                    f2.write(title)
        f2.close()
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
    name = name.lower()
    with open(name + '.txt') as f1:
        lines1 = f1.readlines()
    f1.close()
    if lines1[0] == "p\n":
        with open(name + '.txt', 'w') as f1:
            f1.write(addon+'\n')
        f1.close()
    else:
        with open(name + '.txt', 'a') as f1:
            f1.write(addon+'\n')
        f1.close()


def remove_from_list(name, line):
    name = name.lower()
    with open(name + '.txt') as f1:
        lines1 = f1.readlines()
        print(len(lines1))
    f1.close()
    if int(line) > len(lines1):
        message = "Lista ma tylko "+str(len(lines1))+" wpisów!"
        return message
    with open(name + '.txt', 'w') as f2:
        for index, title in enumerate(lines1, start=1):
            if index != int(line):
                f2.write(title)
    f2.close()
    message = "Usunięto wpis!"
    return message
