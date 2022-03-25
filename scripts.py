import random
import discord
import openpyxl

client = discord.Client()


def commandlist():
    path = "commands.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    message = "Lista moich komend:\n"
    for row in sheet_obj.iter_rows():
        c1 = row[0].value
        c2 = row[1].value
        c3 = row[2].value
        message += (c1 + " - " + c2 + ", argumenty: " + c3 + "\n")
    #print(message)
    wb_obj.save(path)
    return message


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

def new_user_points(p):
    path = "points.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    for row in sheet_obj.rows:
        for cell in row:
            if cell.value == p:
                message = "Już zliczam Twoje punkty!"
                return message
    row_count = int(sheet_obj.max_row) + 1
    cell1 = sheet_obj.cell(row=row_count, column=1)
    cell1.value = p
    cell2 = sheet_obj.cell(row=row_count, column=3)
    cell2.value = 0
    message = "Od teraz punkty użytkownika " + p + "' są już zliczane!"
    wb_obj.save(path)
    return message


def adding_points(p):
    path = "points.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    for row in sheet_obj.rows:
        for cell in row:
            if cell.value == p:
                cell1 = sheet_obj.cell(row=cell.row, column=3)
                c1 = cell1.value
                print(c1)
                c1 += 1
                cell1.value = c1
                print(cell1.value)
                print(type(c1))
            break
    wb_obj.save(path)


def get_points(p):
    path = "points.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active

    for row in sheet_obj.rows:
        for cell in row:
            print(cell.value)
            if p == cell.value:
                cell1 = sheet_obj.cell(row=cell.row, column=3)
                c1 = cell1.value
                #print(c1)
                message = "Amount of points for " + p + " is: " + str(c1)
                wb_obj.save(path)
                return message

    message = "Ten użytkownik nie ma jeszcze zliczanych punktów!"
    wb_obj.save(path)
    return message




