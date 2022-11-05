from itertools import count
from config import bot, dp, bot_id, admins

from aiogram.types import Message, CallbackQuery, ContentTypes

from sql.func import post_sql_query, register_channel, AllUserID
from keyboards.InlineKeyboard import send_btn, can_btn, channelbtn
import asyncio

step = {}


@dp.message_handler(commands=['admin'])
async def adminStart(msg: Message):
    users = post_sql_query('SELECT COUNT(*) FROM users')[0][0]
    await msg.answer(f'Admin Panel\nUsers: {users}', reply_markup=send_btn())


@dp.callback_query_handler(lambda call: call.data == 'cancel')
async def addchannel(call: CallbackQuery):
    step.clear()
    await call.message.delete()
    text = 'canceled'
    await call.message.answer(text)

@dp.callback_query_handler(lambda call: call.data == 'addcha')
async def addchannel(call: CallbackQuery):
    step.update({call.from_user.id: 'addch'})
    text = 'Menga kanaldan bitta post forward qilib yoki kanal id`sini yuboring'
    await call.message.answer(text, reply_markup=can_btn())

@dp.message_handler(lambda message: message.forward_from_chat and step.get(message.chat.id)=='addch', content_types=ContentTypes.ANY)
async def chanfortext(msg: Message):
    getchat = await bot.get_chat_member(msg.forward_from_chat.id, bot_id)
    if getchat.status == 'administrator':
        if register_channel(channel_id=msg.forward_from_chat.id, channel_name=msg.forward_from_chat.title,
                            channel_username=msg.forward_from_chat.username, couunt=0) != '5':
            await bot.send_message(msg.chat.id, 'Kanal muvaffaqiyatli qoshildi')
        else:
            await bot.send_message(msg.chat.id, 'avval kanalga qoshilgan')
    else:
        await bot.send_message(msg.chat.id, 'bot kanalda admin emas!')
    step.clear()

@dp.callback_query_handler(lambda call: call.data == 'delchan')
async def ddelChan(call: CallbackQuery):
    await call.message.answer("📝 Kanallar ro'yxati", reply_markup=channelbtn())

@dp.callback_query_handler(lambda call: 'kanaldel=' in call.data, user_id=admins)
async def Kanaldeltime(call: CallbackQuery):
    x = str(call.data).split('=')[1]
    post_sql_query(f'DELETE FROM CHANNELS WHERE channel_id={x}')
    await bot.edit_message_text('kanallar', call.from_user.id, message_id=call.message.message_id, reply_markup=channelbtn())

@dp.callback_query_handler(lambda call: call.data in ['forward', 'msg'])
async def sendStep(call: CallbackQuery):
    step.update({call.from_user.id: call.data})
    await call.message.answer('Menga post yuboring', reply_markup=can_btn())

@dp.message_handler(lambda message: step.get(message.chat.id)=='forward',content_types=ContentTypes.ANY)
async def sendding(msg: Message):
    count = 0
    nocount = 0
    await msg.answer('Kuting...')
    for u in AllUserID():
        await asyncio.sleep(.05)
        try:
            await bot.forward_message(chat_id=u[0], from_chat_id=msg.chat.id, message_id=msg.message_id)
            count += 1
        except:
            nocount += 1
    await bot.send_message(chat_id=msg.chat.id, text=f'{count}ta odamga xabar yuborildi\n{nocount}ta odamga yuborilmadi')
    step.clear()

@dp.message_handler(lambda message: step.get(message.chat.id)=='msg',content_types=ContentTypes.ANY)
async def seddingmsg(msg: Message):
    count = 0
    nocount = 0
    await msg.answer('Kuting...')
    for u in AllUserID():
        try:
            await bot.copy_message(chat_id=u[0], from_chat_id=msg.chat.id, message_id=msg.message_id, reply_markup=msg.reply_markup)
            count += 1
            await asyncio.sleep(.05)
        except:
            nocount += 1
    await bot.send_message(chat_id=msg.chat.id, text=f'{count}ta odamga xabar yuborildi\n{nocount}ta odamga yuborilmadi')
    step.clear()
