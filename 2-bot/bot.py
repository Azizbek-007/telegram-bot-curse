import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia

wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

# initialization
bot = Bot(token='5766145710:AAHHaHPHM9DKaBaU6z77R5QmD_qLQsGyIYs', parse_mode='markdown')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Assalawma aleykum botqa xosh kelipsiz bul bot arqali siz wikipedia bar maglumatlardi taba alasiz')

@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    if wikipedia.search(text):
        summary = wikipedia.summary(message.text)
        await  message.answer(summary)
    else:  await message.answer("maglumat tabilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)