import telebot
from telebot import types
import shelve
import random
from utils import declensed

bot = telebot.TeleBot("1279033722:AAG4_U4YZuzD5g1MJdqH4d71yubktHx3-Qs")

@bot.message_handler(commands=["start"])
def start_message(message):
	bot.send_message(message.chat.id, "Добро пожаловать в игру тайный Санта!")
	bot.send_message(message.chat.id, "Наши правила: \n1. Денежный лимит подарка - до 500 рублей. \n2. Подарок желательно упаковать так, чтобы не было понятно, что это и какой формы.")
	bot.send_message(message.chat.id, "Введи своё имя и фамилию:")
	bot.register_next_step_handler(message, checker)

def start_again(message):
	bot.send_message(message.chat.id, "Введи своё имя и фамилию:")

participants = ["Ксения Гливко", "Илья Чернигин", "Илья Благодарный", "Антон Терентьев", "Ангелина Лущаева", "Александра Алексеева", "Геннадий Кислов", "Ася Усольцева"]

@bot.message_handler(content_types=["text"])
def checker(message):
	lower_list = map(lambda x: x.lower(), participants)
	if message.text.lower() not in lower_list:
		bot.send_message(message.chat.id, "Ошибочка вышла, перепроверь своё имя, умник... Или умница... Вы имеете право сами определять свой гендер.")
		return start_again(message)
	return appointer(message)

def appointer(message):
	shelveFile = shelve.open("ShelveFile")
	if message.text.lower() in shelveFile.keys():
		bot.send_message(message.chat.id, "Ты уже знаешь свою жертву! Не пиши мне больше!")
		return
	options = [i for i in participants if i.lower() != message.text.lower() and i.lower() not in shelveFile.values()]
	selection = random.choice(options)
	key = message.text.lower()
	shelveFile[key] = selection.lower()
	bot.send_message(message.chat.id, "Ты тайный Санта для {}, поздравляю!".format(declensed(selection)))
	shelveFile.update()
	shelveFile.close()

if __name__ == "__main__":
	bot.infinity_polling(True)
