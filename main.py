import qrcode
import telebot
from telebot import types
import io
from fn import generate_qr

API_TOKEN = '6919402927:AAFjZDcCGDliYEKTlHStPgUeDbful12aoqw'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('Отправить текс')
    item2 = types.KeyboardButton('Отправить ссылку')
    item3 = types.KeyboardButton('Отправить геопозицию')
    item4 = types.KeyboardButton('Отправить контакт')
    markup.add(item1, item2, item3, item4)

    bot.reply_to(message, "Привет! Выберите тип данных для отправки:", reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Доступные команды /help, /settings')


@bot.message_handler(commands=['settings'])
def change_settings(messsage):
    pass


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    data = message.text
    qr_bytes_io = io.BytesIO()

    qr = qrcode.QRCode(
        version=1,
        border=4,
        box_size=10,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(qr_bytes_io)
    qr_bytes_io.seek(0)

    bot.send_photo(message.chat.id, qr_bytes_io)


if __name__ == '__main__':
    bot.polling(none_stop=True)
