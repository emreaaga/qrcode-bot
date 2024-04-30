import telebot

from fn import generate_qr
from buttons import *

API_TOKEN = '6919402927:AAFjZDcCGDliYEKTlHStPgUeDbful12aoqw'

bot = telebot.TeleBot(API_TOKEN)

previous_menu = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет!")


@bot.message_handler(commands=['settings'])
def change_settings(message):
    bot.send_message(message.chat.id, 'Что настроим:', reply_markup=create_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global previous_menu
    if call.data == 'back_color':
        previous_menu[call.message.chat.id] = create_menu()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите цвет фона:")
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      reply_markup=create_menu_with_colors())
    elif call.data == 'set_version':
        previous_menu[call.message.chat.id] = create_menu()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите версию:")
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      reply_markup=create_menu_with_versions())

    elif call.data == 'back':
        previous_keyboard = previous_menu.get(call.message.chat.id)
        if previous_keyboard:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите действие:", reply_markup=previous_keyboard)
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="Вы уже находитесь в основном меню.")


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
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
