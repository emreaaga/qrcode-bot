from telebot import types


def create_menu():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Цвет", callback_data='back_color'),
        types.InlineKeyboardButton("Версия", callback_data='set_version')
    )
    return keyboard


def create_menu_with_colors():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Черный", callback_data='black'),
        types.InlineKeyboardButton("Белый", callback_data='white')
    )
    keyboard.row(
        types.InlineKeyboardButton("Синий", callback_data='blue'),
        types.InlineKeyboardButton("Зеленый", callback_data='green')
    )
    keyboard.row(types.InlineKeyboardButton("Назад", callback_data='back'))
    return keyboard


def create_menu_with_versions():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton('version 1.0', callback_data='version1'),
        types.InlineKeyboardButton('version 1.3', callback_data='version2')
    )
    keyboard.row(
        types.InlineKeyboardButton('version 1.4', callback_data='version3'),
        types.InlineKeyboardButton('version 1.9', callback_data='version4')
    )
    keyboard.row(types.InlineKeyboardButton('Назад', callback_data='back'))
    return keyboard
