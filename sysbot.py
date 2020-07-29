import telebot

bot = telebot.TeleBot('1338073509:AAEEb3cHyOS2-BPuwiEPKhGBl8g0laZSKRw')

@bot.message_handler(commands=['start'])
def start(message):
	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!"
	bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)