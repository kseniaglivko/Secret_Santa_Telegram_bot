import telebot
from telebot import types
import shelve
import random
from utils import declensed, name_checked

bot = telebot.TeleBot("1279033722:AAG4_U4YZuzD5g1MJdqH4d71yubktHx3-Qs")

@bot.message_handler(commands=["start"])
def start_message(message):
	bot.send_message(message.chat.id, "Добро пожаловать в игру тайный Санта!")
	bot.send_message(message.chat.id, "Наши правила: \n1. Денежный лимит подарка - до 500 рублей. \n2. Подарок желательно упаковать так, чтобы не было понятно, что это и какой формы.")
	bot.send_message(message.chat.id, "Введи своё имя и фамилию:")
	bot.register_next_step_handler(message, checker)

def start_again(message):
	bot.send_message(message.chat.id, "Введи своё имя и фамилию:")

participants = ["Ксения Гливко", "Илья Чернигин", "Илья Благодарный", "Антон Терентьев", "Ангелина Лущаева", "Александра Алексеева", "Геннадий Кислов", "Ася Усольцева", "Мария Куликова", "Александр Панасюк"]

@bot.message_handler(content_types=["text"])
def checker(message):
	text = name_checked(message.text)
	lower_list = map(lambda x: x.lower(), participants)
	if text not in lower_list:
		bot.send_message(message.chat.id, "Ошибочка вышла, перепроверь своё имя, умник... Или умница... Вы имеете право сами определять свой гендер.")
		return start_again(message)
	return appointer(message)

def appointer(message):
	text = name_checked(message.text)
	shelveFile = shelve.open("ShelveFile")
	if text in shelveFile.keys():
		bot.send_message(message.chat.id, "Ты уже знаешь свою жертву! Не пиши мне больше!")
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAKFd1_aJYoYk1XqUPS94w2LnVv57LImAAJ7AwACbbBCA1tz5hS9rf3YHgQ")
		return
	options = [i for i in participants if i.lower() != text and i.lower() not in shelveFile.values()]
	selection = random.choice(options)
	shelveFile[text] = selection.lower()
	bot.send_message(message.chat.id, "Ты тайный Санта для {}, поздравляю!".format(declensed(selection)))
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAKFcV_aJTLNLLmTFNeZxQWQ-KPK7qtsAAJjAwACbbBCA-FJL7WrGAjMHgQ")
	shelveFile.update()
	shelveFile.close()

if __name__ == "__main__":
	bot.infinity_polling(True)
