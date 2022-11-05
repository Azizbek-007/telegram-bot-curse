from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = KeyboardButton("🈳 Переводчик")
    # btn3 = KeyboardButton("📄 Qo'llanma")
    markup = btn.add(btn2)
    # markup = btn.add(btn3)
    return markup