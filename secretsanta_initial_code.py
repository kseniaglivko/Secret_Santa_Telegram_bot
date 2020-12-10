import shelve # We're going to create an inbuilt database to remember people who were assigned to their Santas

shelveFile = shelve.open('mydata') # Creating a file to store assignments

import random

participants = ['Ксения Гливко', 'Илья Чернигин', 'Илья Благодарный', 'Антон Терентьев', 'Ангелина Лущаева', 'Александра Алексеева', 'Геннадий Кислов']
template = 'Ты тайный Санта для {}, поздравляю!'

def declensed(fullname):
# Russian names must be declensed. I know it could be done via pymorphy2, but I wanted to practice by creating my own code..
    lst = fullname.split(' ')
    name = lst[0]
    surname = lst[1]
    last_char_name = lst[0][-1]
    last_char_surname = lst[1][-1]
    if last_char_name == 'я':
        if last_char_surname == 'н':
            lst = name[:-1] + 'и ' + surname + 'а'
        elif last_char_surname == 'й':
            lst = name[:-1] + 'и ' + surname[:-2] + 'ого'
        else:
            lst = name[:-1] + 'и ' + surname
    elif last_char_name and last_char_surname == 'а':
        lst = name[:-1] + 'ы ' + surname[:-1] + 'oй'
    elif last_char_surname == 'в':
        if last_char_name == 'н':
            lst = name + 'a ' + surname + 'a'
        elif last_char_name == 'й':
            lst = name[:-1] + 'я '+ surname + 'a'
    return str(lst)

def appointer(fullname): # This is the part of code that assigns people to their Santas
    if fullname not in participants:
        if fullname == 'Ксюша Гливко': # Once again, is Russian there are shortenings for names, so I've added this cycle so the bot could accept every version of a name.
            return appointer('Ксения Гливко')
        elif fullname == 'Саша Алексеева':
            return appointer('Александра Алексеева')
        elif fullname == 'Гена Кислов':
            return appointer('Геннадий Кислов')
        print('Ошибочка вышла, перепроверь своё имя, умник... Или умница... Вы имеете право сами определять свой гендер.')
        return
    if fullname in shelveFile.keys(): # As the assignees are being written into our database, we should check if a person already has an assignee
        print('Ты уже знаешь свою жертву!')
        return
    options = [i for i in participants if i != fullname and i not in shelveFile.values()]
# Checking that a person wouldn't be assigned to him- or herself and wouldn't be assigned to a person who already has their Santa
    selection = random.choice(options)
    shelveFile[fullname] = selection # Writing the selection to our database
    print(template.format(declensed(selection)))
    print(list(shelveFile.items()))

if __name__ == '__main__':
    print('Добро пожаловать в игру тайный Санта! \nНаши правила: \n1. Денежный лимит подарка - до 500 рублей. \n2. Подарок желательно упаковать так, чтобы не было понятно, что это и какой формы. \n')
    print('Итак, начнем!\n')
    appointer(fullname = (input('Введи своё имя и фамилию: ').lower().title()))

shelveFile.close() # Shutting down our database
