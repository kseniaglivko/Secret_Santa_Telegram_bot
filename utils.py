participants_surnames = {
    "гливко": "ксения гливко",
    "чернигин": "илья чернигин",
    "благодарный": "илья благодарный",
    "терентьев": "антон терентьев",
    "лущаева": "ангелина лущаева",
    "алексеева": "александра алексеева",
    "кислов": "геннадий кислов",
    "усольцева": "ася усольцева",
    "куликова": "мария куликова",
    "панасюк": "александр панасюк",
}


def get_declensed_name(fullname):
    """Returns denclensed name for the final message with the info about Secret Santa's appointee"""
    lst = fullname.split(" ")
    name = lst[0]
    surname = lst[1]
    last_char_name = lst[0][-1]
    last_char_surname = lst[1][-1]
    if last_char_name == "я":
        if last_char_surname == "н":
            lst = name[:-1] + "и " + surname + "а"
        elif last_char_surname == "й":
            lst = name[:-1] + "и " + surname[:-2] + "ого"
        elif last_char_surname == "а":
            lst = name[:-1] + "и " + surname[:-1] + "oй"
        else:
            lst = name[:-1] + "и " + surname
    elif last_char_name and last_char_surname == "а":
        lst = name[:-1] + "ы " + surname[:-1] + "oй"
    elif last_char_surname == "в":
        if last_char_name == "н":
            lst = name + "a " + surname + "a"
        elif last_char_name == "й":
            lst = name[:-1] + "я " + surname + "a"
    elif last_char_surname == "к":
        lst = name + "a " + surname + "a"
    return str(lst)


def get_proper_name(message):
    """Returns the full form of the name to enable the use of diminutive names and such"""
    try:
        fullname = message.split(" ")
    except AttributeError:
        return "некорректное имя"
    else:
        for el in fullname:
            if el not in participants_surnames.keys():
                continue
            return participants_surnames.get(el)
