import telebot

from fn import *
from buttons import *


API_TOKEN = 'TK'

bot = telebot.TeleBot(API_TOKEN)
color, vr = 'white', 1
previous_menu = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, '''🇺🇸 Great! Just send me anything to generate QR-code!
🇷🇺 Отлично! Просто пришлите мне что-нибудь, чтобы получить QR-код!''')


@bot.message_handler(commands=['settings'])
def change_settings(message):
    bot.send_message(message.chat.id, 'Что настроим:', reply_markup=create_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global previous_menu, color, vr
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
    elif call.data.startswith('color_'):
        color = call.data.split('_')[1]
        bot.answer_callback_query(callback_query_id=call.id, text=f"Вы выбрали цвет {color}.")

    elif call.data.startswith('version_'):
        vr = int(call.data.split('_')[1])
        print(vr)
        bot.answer_callback_query(callback_query_id=call.id,
                                  text=f"Вы выбрали версию {' '.join(call.data.split('_'))}.")


@bot.message_handler(content_types=['text'])
def send_link_qr(message):
    global color
    qr_code = generate_qr(message.text, backcolor=color, vr=vr)
    bot.send_photo(message.chat.id, qr_code)


@bot.message_handler(content_types=['location'])
def send_location_qr(message):
    global color
    latitude = message.location.latitude
    longitude = message.location.longitude
    qr_code = generate_qr(message.text, latitude, longitude, backcolor=color, vr=vr)
    bot.send_photo(message.chat.id, qr_code)


@bot.message_handler(content_types=['contact'])
def send_contact_qr(message):
    qr_code = generate_qr(message.contact.phone_number, backcolor=color, vr=vr)
    bot.send_photo(message.chat.id, qr_code)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, 'Currently dont support image operation')

if __name__ == '__main__':
    bot.polling(none_stop=True)
