import telebot
from telebot import types
import shelve
import random
from utils import get_declensed_name, get_proper_name

bot = telebot.TeleBot("<TOKEN_HERE>")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в игру тайный Санта!")
    bot.send_message(
        message.chat.id,
        "Наши правила: \n1. Денежный лимит подарка - до 500 рублей. \n2. Подарок желательно упаковать так, чтобы не было понятно, что это и какой формы.",
    )
    bot.send_message(message.chat.id, "Введи своё имя и фамилию:")
    bot.register_next_step_handler(message, check_if_in_list)


def start_again(message):
    """Called in case of an input error"""
    bot.send_message(message.chat.id, "Введи своё имя и фамилию:")


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


@bot.message_handler(content_types=["text"])
def check_if_in_list(message):
    """Checks for the user's name to be in the participants list"""
    text = get_proper_name(message.text)
    if text not in participants:
        bot.send_message(
            message.chat.id,
            "Ошибочка вышла, перепроверь своё имя, умник... Или умница... Вы имеете право сами определять свой гендер.",
        )
        return start_again(message)
    return appoint_victim_for_santa(message)


def appoint_victim_for_santa(message):
    """Appoints a 'victim' for the Secret Santa and writes the two names in the db"""
    text = get_proper_name(message.text)
    shelveFile = shelve.open("ShelveFile")
    if text in shelveFile.keys():
        bot.send_message(
            message.chat.id, "Ты уже знаешь свою жертву! Не пиши мне больше!"
        )
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAKFd1_aJYoYk1XqUPS94w2LnVv57LImAAJ7AwACbbBCA1tz5hS9rf3YHgQ",
        )
        return
    options = [i for i in participants if i != text and i not in shelveFile.values()]
    selection = random.choice(options)
    shelveFile[text] = selection
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
    shelveFile.update()
    shelveFile.close()
