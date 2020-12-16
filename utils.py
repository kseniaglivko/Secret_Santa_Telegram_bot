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
    return str(lst)
