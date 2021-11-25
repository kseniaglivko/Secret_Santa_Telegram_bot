# Secret Santa Telegram bot
This is a telegram bot to dynamically assign Secret Santas to a specific list of participants 

**Note**: the bot was created to be used with russian names. 

Bot is case insensitive and understands diminutive names.



## Description

1.  User types in his/her name, then the name is checked to be in the participants list. If it is not in the list - bot throws an error.
2. Then the name is checked to be in the database - to check whether the user already has an asignee. If the person enters his/her name twice - bot throws an error. 
3. After checking, bot assigns a name from the participants list to the user, displays the name and a sticker to the user. While assigning, bot excludes the user's name from selection.
4. Bot uploads information about Santa and his/hers asignee to the database so the same person wouldn't be assigned twice.


## Installation

1. You need to create a telegram bot and get API Token. See more information here: https://core.telegram.org/bots

2. ```git clone https://github.com/kseniaglivko/Secret_Santa_Telegram_bot.git```

3. Open the project in IDE and set up virtual environment.

4. ```pip install -r requirements.txt```

5. Insert your API token in ```bot``` variable in bot.py line 7.

6. Before using it you may want to update names in ```participants_surnames``` variable in utils.py and in ```participants``` variable in bot.py, modify ```get_declensed_name``` function in utils.py and so on. You are welcome to modify the code for your own needs.

7. Go to project directory, open terminal and run ```python3 main.py```

Bot will be active while the terminal is running.


## Tests

"tests" directory contains some unittests you may run to check if bot works properly.
