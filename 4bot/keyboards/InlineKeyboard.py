from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from sql.func import post_sql_query
def send_btn():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('➕Add channel', callback_data='addcha'))
    markup.add(InlineKeyboardButton('➖del channel', callback_data='delchan'))
    markup.add(InlineKeyboardButton('Send Message', callback_data='msg'))
    markup.add(InlineKeyboardButton('Send Forward', callback_data='forward'))
    return markup

def can_btn():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('cancel', callback_data='cancel'))
    return markup

def channelbtn():
    us = post_sql_query("SELECT * FROM CHANNELS")
    markup = InlineKeyboardMarkup(row_width=2)
    i = 0
    for r in us:
        i +=1
        r1 = r[1].replace('@', '')
        r1 = 'https://t.me/' + r1
        btn = InlineKeyboardButton(text=f"{r[2]}", url=r1)
        btnn = InlineKeyboardButton('❌', callback_data=f'kanaldel={r[0]}')
        markup.add(btn, btnn)
    return markup

def channel_btn():
    us = post_sql_query("SELECT * FROM CHANNELS")
    markup = InlineKeyboardMarkup(row_width=2)
    i = 0
    for r in us:
        i +=1
        r1 = r[1].replace('@', '')
        r1 = 'https://t.me/' + r1
        btn = InlineKeyboardButton(text=f"{i}- kanalga a'zo bo'ling", url=r1)
        markup.add(btn)
    btn2 = InlineKeyboardButton('🔔 Tekshirish ', callback_data='chek')
    markup.add(btn2)
    return markup

a = ['🇮🇹 Italian', '🇹🇯 tajik', '🇱🇻 latvian','🇺🇦 Ukrainian', '🇺🇿 Uzbek', '🇷🇺 Russian', '🏴󠁧󠁢󠁥󠁮󠁧󠁿 English', '🇨🇳 China', '🇰🇷 Korean', '🇹🇷 Turk', '🇸🇦 Arab', 'Karakalpak']
b = ['lan-it', 'lan-tg', 'lan-lv', 'lan-uk', 'lan-uz',   'lan-ru',     'lan-en',     'lan-zh-cn', 'lan-ko',   'lan-tr', 'lan-ar', 'lan-kaa']

def langs_btn():
    lis = []
    markup = InlineKeyboardMarkup(row_width=2)
    for q, w in zip(a, b):
        button = InlineKeyboardButton(text=q, callback_data=w)
        lis.append(button)
    return markup.add(*lis)