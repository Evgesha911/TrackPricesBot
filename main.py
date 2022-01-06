import telebot
import config

bot=telebot.TeleBot('5096778027:AAEuJNf-CCydjEQt04kYkpSJOQ6_4PGAD4A')

@bot.message_handler(content_types=['text'])
def welcome(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
