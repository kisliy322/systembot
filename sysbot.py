import telebot

bot = telebot.TeleBot('api')

@bot.message_handler(commands=['start'])
def start(message):
	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!"
	bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)
