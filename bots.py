import telebot
from telebot import types
import shelve
import random
from utils import declensed

bot = telebot.TeleBot("<YOUR TOKEN HERE>")

@bot.message_handler(commands=["start"])
def start_message(message):
	bot.send_message(message.chat.id, "Добро пожаловать в игру тайный Санта!")
	bot.send_message(message.chat.id, "Наши правила: \n1. Денежный лимит подарка - до 500 рублей. \n2. Подарок желательно упаковать так, чтобы не было понятно, что это и какой формы.")
	bot.send_message(message.chat.id, "Введи своё имя и фамилию:")
	bot.register_next_step_handler(message, checker)

def start_again(message):
	bot.send_message(message.chat.id, "Введи своё имя и фамилию:")

participants = ["Ксения Гливко", "Илья Чернигин", "Илья Благодарный", "Антон Терентьев", "Ангелина Лущаева", "Александра Алексеева", "Геннадий Кислов"]

@bot.message_handler(content_types=["text"])
def checker(message):
	if message.text not in participants:
		if message.text == "Ксюша Гливко":
			return appointer("Ксения Гливко")
		elif message.text == "Саша Алексеева":
			return appointer("Александра Алексеева")
		elif message.text == "Гена Кислов":
			return appointer("Геннадий Кислов")
		bot.send_message(message.chat.id, "Ошибочка вышла, перепроверь своё имя, умник... Или умница... Вы имеете право сами определять свой гендер.")
		return start_again(message)
	return appointer(message)

def appointer(message):
	shelveFile = shelve.open("ShelveFile")
	if message.text in shelveFile.keys():
		bot.send_message(message.chat.id, "Ты уже знаешь свою жертву! Не пиши мне больше!")
		return
	options = [i for i in participants if i != message.text and i not in shelveFile.values()]
	selection = random.choice(options)
	key = message.text
	shelveFile[key] = selection
	bot.send_message(message.chat.id, "Ты тайный Санта для {}, поздравляю!".format(declensed(selection)))
	shelveFile.update()
	shelveFile.close()

if __name__ == "__main__":
	bot.infinity_polling(True)
