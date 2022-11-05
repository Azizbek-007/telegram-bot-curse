import os
import urllib.parse
from config import bot, dp
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.builtin import CommandStart

from googletrans import Translator
from sql.func import register_user, channel_ids
from keyboards.InlineKeyboard import channel_btn, langs_btn, a, b
from keyboards.ReplyKeyboard import start_btn
from test import QQ_TO_UZ

async def joinChan(bot, msg):
    resut = []
    for x in channel_ids():
        g = await bot.get_chat_member(x, msg.from_user.id)
        resut.append(g.status)
    if 'left' in resut:
        await bot.send_message(msg.from_user.id, f"Assalomu alaykum {msg.from_user.first_name}. Botni ishga tushurish uchun kanallarga a'zo bo'ling va a'zolikni tekshirish buyrug'ini bosing.", reply_markup=channel_btn())
    else:
        return True

@dp.callback_query_handler(text='chek')
async def chanellstatuschek(call: CallbackQuery):
    resut = []
    for x in channel_ids():
        g = await bot.get_chat_member(x, call.from_user.id)
        resut.append(g.status)
    if 'left' in resut:
        await call.answer("iltimos kanallarga a'zo bo'ling!")
    else:
        await call.message.delete()
        await call.message.answer("*Kerakli bo\'limni tanlang* 👇", 'markdown', reply_markup=start_btn())

@dp.message_handler(CommandStart())
@dp.throttled(rate=1)
async def hello(msg: Message):
    register_user(msg.from_user.id, msg.from_user.username, first_name=msg.from_user.first_name, last_name=msg.from_user.last_name)    
    await msg.reply('*Выберите нужный раздел* 👇', 'markdown', reply_markup=start_btn())

@dp.message_handler(text='🈳 Переводчик')
@dp.throttled(rate=1)
async def Tarjimon(msg: Message):
    if await joinChan(bot, msg) == True:
        await msg.answer('<b>1.Выберите язык, который вы хотите перевести</b>', 'HTML', reply_markup=langs_btn())

# @dp.message_handler(text='📄 Qo\'llanma')
# async def Tarjimon(msg: Message):
#     await msg.reply('''⚡️*Assalomu alaykum aziz foydalanuvchi "Tarjimon" boʻlimidan foydalanish uchun*

# ```
# ° Tarjimon boʻlimiga kirasiz
# ° Kiritmoqchi boʻlgan tilni tanlaysiz 
# ° Tarjima qilish uchun tilni tanlaysiz
# ° Rasim yoki matin yuborasiz ```

# *Bizni tanlaganingiz uchun rahmat*''', 'markdown', reply_markup=start_btn())

lan1 = {}
lan2 = {}

@dp.message_handler(lambda message: lan1.get(message.from_user.id) and lan2.get(message.from_user.id))
@dp.throttled(rate=1)
async def tar_api(msg: Message):
    await msg.answer_chat_action('typing')
    til1 = lan1.get(msg.from_user.id)
    til2 = lan2.get(msg.from_user.id)
    if til1 == 'kaa' or til2 == 'kaa':
        result = QQ_TO_UZ(msg.text, til1, til2)
        await msg.reply(result)
    else:
        translator = Translator()
        result = translator.translate(msg.text, dest=til2, src=til1).text
        try:
            print(result)
            await msg.answer_chat_action('record_voice')
            url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=gtx&q={urllib.parse.quote(result)}&tl={til2}"
            await msg.answer_audio(url, caption=f'<code>{result}</code>', parse_mode='html')
        except:
            await msg.answer(f"<code>{result}</code>", parse_mode='html', reply_markup=start_btn())
            
        

@dp.callback_query_handler(lambda call: '2lan-' in call.data)
async def til_2(call: CallbackQuery):
    x = call.data.replace("2lan-", "")
    y = str(call.data).split("|")[1]
    f = y.replace("lan-", "")
    x = x.replace(f"|{y}", "")

    lan1.update({call.from_user.id: f})
    lan2.update({call.from_user.id: x})
    
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await bot.send_message(call.message.chat.id, "*Отправить утренник для перевода: *", 'markdown')

@dp.callback_query_handler(lambda call: 'lan-' in call.data)
async def tarjimon_btn(call):
    data = call.data
    inid = b.index(data)
    res = [item.replace(a[inid], '✅' + a[inid]) for item in a]
    if data == 'lan-kaa': 
        res = [a[0], f'✅ {a[inid]}']
    elif str(data) != 'lan-uz':
        a.remove('Karakalpak') 
        b.remove('lan-kaa')
    lis = []
    markup = InlineKeyboardMarkup(row_width=2)
    for x, y in zip(res, b):
        button = InlineKeyboardButton(text=x, callback_data=f"2{y}|{call.data}")
        lis.append(button)
    x = call.data.replace("lan-", "")
    await bot.edit_message_text('<b>2.Выберите язык, который вы хотите перевести: </b>', call.from_user.id, call.message.message_id, parse_mode='html', reply_markup=markup.add(*lis))