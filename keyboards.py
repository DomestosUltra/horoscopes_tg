from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


def main_inline_kb() -> InlineKeyboardMarkup:
    bd = InlineKeyboardBuilder()
    bd.button(text='Получить гороскоп', callback_data='get_horo')
    bd.button(text='Заполнить анкету', callback_data='load_form')
    bd.button(text='Подписка', callback_data='subscribe')
    bd.button(text='Отзывы/Пожелания', callback_data='rate')
    bd.adjust(1, 1)
    return bd.as_markup()


def back_1() -> InlineKeyboardMarkup:
    bd = InlineKeyboardBuilder()
    bd.button(text="Назад", callback_data='back_1')
    return bd.as_markup()


def choose_gender() -> InlineKeyboardMarkup:
    bd = InlineKeyboardBuilder()
    bd.button(text='Женщина', callback_data='woman')
    bd.button(text='Мужчина', callback_data='man')
    bd.adjust(2, 1)
    return bd.as_markup()


# ✅
# 🚫
def choose_cat() -> InlineKeyboardBuilder:
    bd = InlineKeyboardBuilder()
    bd.button(text='cat 1 🚫', callback_data='cat 1 🚫')
    bd.button(text='cat 2 🚫', callback_data='cat 2 🚫')
    bd.button(text='cat 3 🚫', callback_data='cat 3 🚫')
    bd.button(text='Применить', callback_data='confrim')
    bd.adjust(1, 1)
    return bd


def rate_inline_kb() -> InlineKeyboardMarkup:
    bd = InlineKeyboardBuilder()
    for i in range(1, 6):
        bd.button(text=f'{i}', callback_data=f'rate_{i}')
    bd.button(text='Назад', callback_data='back_1')
    bd.adjust(5, 2)
    return bd.as_markup()


def choose_sub() -> InlineKeyboardBuilder:
    bd = InlineKeyboardBuilder()
    bd.button(text='Подписка 1', callback_data='Подписка 1')
    bd.button(text='Подписка 2', callback_data='Подписка 2')
    bd.button(text='Подписка 3', callback_data='Подписка 3')
    bd.button(text='Назад', callback_data='back_1')
    bd.adjust(1, 1)
    return bd


