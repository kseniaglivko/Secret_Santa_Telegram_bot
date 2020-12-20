def declensed(fullname):
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
        elif last_char_surname == 'а':
            lst = name[:-1] + 'и ' + surname[:-1] + 'oй'
        else:
            lst = name[:-1] + 'и ' + surname
    elif last_char_name and last_char_surname == 'а':
        lst = name[:-1] + 'ы ' + surname[:-1] + 'oй'
    elif last_char_surname == 'в':
        if last_char_name == 'н':
            lst = name + 'a ' + surname + 'a'
        elif last_char_name == 'й':
            lst = name[:-1] + 'я '+ surname + 'a'
    elif last_char_surname == 'к':
        lst = name + 'a ' + surname + 'a'
    return str(lst)

def name_checked(name):
    if "гливко" in name.lower():
        return "ксения гливко"
    elif "алексеева" in name.lower():
        return "александра алексеева"
    elif "кислов" in name.lower():
        return "геннадий кислов"
    elif "усольцева" in name.lower():
        return "ася усольцева"
    elif "чернигин" in name.lower():
        return "илья чернигин"
    elif "благодарный" in name.lower():
        return "илья благодарный"
    elif "лущаева" in name.lower():
        return "ангелина лущаева"
    elif "терентьев" in name.lower():
        return "антон терентьев"
    elif "куликова" in name.lower():
        return "мария куликова"
    elif "панасюк" in name.lower():
        return "александр панасюк"
    return name.lower()
