# Secret_Santa_Telegram_bot
Telegram Bot to dynamically assign Secret Santas for a specific list of participants. Language: Russian

This Bot is not universal - it works with a specific list of names.

    Works only with a specific list of participants.
    User types in his/her name, then the names is checked to be in the participants list. If it is not in the list - bot gives an error.
    The name is checked to be in the database - to check whether the person already has an asignee. If the person enters his/her name twice - bot gives an error.
    After checking, bot assigns a name from the participants list and uploads information about Santa and the asignee to the database so the same name wouldn't be assigned twice or the person wouldn't be assigned to his/herself.

Bot is case insensitive. Bot takes diminutive names.
