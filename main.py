import telebot
from telebot import types
import config

bot=telebot.TeleBot('5096778027:AAEuJNf-CCydjEQt04kYkpSJOQ6_4PGAD4A')


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    about_btn = types.InlineKeyboardButton(text="1.Хочу узнать как это работает", callback_data='1')
    surch_btn = types.InlineKeyboardButton(text="2.Хочу найти выгодную цену", callback_data='2')
    keyboard.add(about_btn)
    keyboard.add(surch_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="В этом сервисе, представлены десятки тысяч товаров. "
                                                                                                         "Можно сравнить стоимость конкретного продукта в разных сетях или изучить всю категорию."
                                                                                                         " Пока мы оцифровали ассортимент четырех крупных ритейлеров – «Евроопт», «Гиппо», «Корона» и «Green».")

        if call.data == "2":
            @bot.message_handler(content_types=["text"])
            def default_test(message):
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="Перейти на Инфопрайс", url="https://infoprice.by/")
                keyboard.add(url_button)
                bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.",
                                 reply_markup=keyboard)




if __name__=="__main__":
	bot.polling(none_stop=True, interval=0)