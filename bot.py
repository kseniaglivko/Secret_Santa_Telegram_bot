"""Module contains full bot logic."""

import telebot  # type: ignore
import shelve
import random

from utils import get_declensed_name, get_proper_name

bot = telebot.TeleBot("<TOKEN_HERE>")

participants = [
    "ксения гливко",
    "илья чернигин",
    "илья благодарный",
    "антон терентьев",
    "ангелина лущаева",
    "александра алексеева",
    "геннадий кислов",
    "ася усольцева",
    "мария куликова",
    "александр панасюк",
]


@bot.message_handler(commands=["start"])
def start_bot(message):
    """After bot is activated, it sends welcome message, asks for user's name and waits for the next step."""
    bot.send_message(message.chat.id, "Добро пожаловать в игру тайный Санта!")
    bot.send_message(
        message.chat.id,
        "Наши правила: \n1. Денежный лимит подарка - до 500 рублей."
        "\n2. Подарок желательно упаковать так, чтобы не было понятно, "
        "что это и какой формы.",
    )
    bot.send_message(message.chat.id, "Введи своё имя и фамилию:")
    bot.register_next_step_handler(message, check_if_username_is_in_list)


def start_again(message):
    """Called in case of an input error."""
    bot.send_message(message.chat.id, "Введи своё имя и фамилию:")


@bot.message_handler(content_types=["text"])
def check_if_username_is_in_list(message):
    """Check for the user's name to be in the participants list."""
    user_name = get_proper_name(message)
    if user_name not in participants:
        bot.send_message(
            message.chat.id,
            "Ошибочка вышла, перепроверь своё имя, умник... "
            "Или умница... Вы имеете право сами определять свой гендер.",
        )
        return start_again(message)
    return assign_santa_to_person(message)


def assign_santa_to_person(message):
    """Assign user as Secret Santa to one of the participants and writes the two names in the db."""
    user_name = get_proper_name(message.text)
    shelve_file = shelve.open("ShelveFile")
    if user_name in shelve_file.keys():
        bot.send_message(
            message.chat.id, "Ты уже знаешь свою жертву! Не пиши мне больше!"
        )

        # This part sends a sticker.
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAKFd1_aJYoYk1XqUPS94w2LnVv57LImAAJ7AwACbbBCA1tz5hS9rf3YHgQ",
        )
        # You may put another sticker id as an argument here.
        return

    options = [
        name
        for name in participants
        if name != user_name and name not in shelve_file.values()
    ]
    selection = random.choice(options)
    shelve_file[user_name] = selection
    bot.send_message(
        message.chat.id,
        "Ты тайный Санта для {}, поздравляю!".format(
            get_declensed_name(selection).title()
        ),
    )
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAKFcV_aJTLNLLmTFNeZxQWQ-KPK7qtsAAJjAwACbbBCA-FJL7WrGAjMHgQ",
    )
    shelve_file.update()
    shelve_file.close()
