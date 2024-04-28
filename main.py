import telebot
from fn import generate_qr
from telebot import types

API_TOKEN = '6919402927:AAFjZDcCGDliYEKTlHStPgUeDbful12aoqw'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Выберите тип данных для отправки:")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Доступные команды /help, /settings')


@bot.message_handler(commands=['settings'])
def change_settings(message):
    pass


@bot.message_handler(content_types=['text'])
def send_link_qr(message):
    qr_code = generate_qr(message.text)
    bot.send_photo(message.chat.id, qr_code)


@bot.message_handler(content_types=['location'])
def send_location_qr(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    qr_code = generate_qr(message.text, latitude, longitude)
    bot.send_photo(message.chat.id, qr_code)


@bot.message_handler(content_types=['contact'])
def send_contact_qr(message):
    qr_code = generate_qr(message.contact.phone_number)
    bot.send_photo(message.chat.id, qr_code)


@bot.message_handler(content_types=['photo'])
def send_photo_qr(message):
    qr_code = generate_qr(None, photo=message)
    bot.send_photo(message.chat.id, qr_code)


if __name__ == '__main__':
    bot.polling(none_stop=True)
