import telebot

bot = telebot.TeleBot("5682572506:AAGClfH5KX4g6ttKvJMITHYjLVYxzGmUxek")

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id, message)



bot.polling(none_stop=True)
