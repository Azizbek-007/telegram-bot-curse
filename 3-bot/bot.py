import logging
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_cyrillic, to_latin

logging.basicConfig(level=logging.INFO)

# initialization
bot = Bot(token='5630487322:AAFmBSYB3sJdcAFbsxkDD86dIxRRBgzdwMc', parse_mode='markdown')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Привет, привет. Я перевод кириллицу на латиницу или наоборот. Введите текст...')

@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    anwer = to_latin(text) if text.isspace() else to_cyrillic(text)
    await message.reply(anwer)

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)