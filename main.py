import telebot
from fn import generate_qr

API_TOKEN = '6919402927:AAFjZDcCGDliYEKTlHStPgUeDbful12aoqw'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Выберите тип данных для отправки:")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Доступные команды /help, /settings')


@bot.message_handler(commands=['settings'])
def change_settings(messsage):
    pass


@bot.message_handler(content_types=['text'])
def send_link_qr(message):
    qr_code = generate_qr(message)
    bot.send_photo(message.chat.id, qr_code)


@bot.message_handler(content_types=['location'])
def send_location_qr(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    qr_code = generate_qr(message, latitude, longitude)
    bot.send_photo(message.chat.id, qr_code)


if __name__ == '__main__':
    bot.polling(none_stop=True)
