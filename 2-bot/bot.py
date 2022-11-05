import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia

wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

# initialization
bot = Bot(token='5695738257:AAF-gKQ41ON2s4qq2OnCk_AEf0zpBsAYoVM', parse_mode='markdown')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Botga xush kelibsiz. Vikipediyada ma\'lumot qidirishda sizga yordam beraman kerakli ma\'lumotlarni kiriting')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer_chat_action('typing')
    text = message.text
    try:
        if wikipedia.search(text):
            summary = wikipedia.summary(message.text)
            print(summary)
            await  message.answer(summary[:1000] + '...')
        else:  await message.answer("ma'lumot topilmadi")
    except: await message.answer("ma'lumot topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)