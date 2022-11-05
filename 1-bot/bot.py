# logger
import logging
# aiogram fremwork in imported Bot, Dispatcher, types
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

# initialization
bot = Bot(token='5766145710:AAHHaHPHM9DKaBaU6z77R5QmD_qLQsGyIYs', parse_mode='markdown')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_id
    await bot.send_message(
        user_id, 
        f'your chat id: ```{user_id}```', 
        reply_to_message_id=message.message_id)

@dp.message_handler(lambda message: message.forward_from)
async def forward_message(message: types.Message):
    user_id = message.from_id
    forward_id = message.forward_from.id
    await bot.send_message(
        user_id, 
        f'chat id: ```{forward_id}```',
        reply_to_message_id=message.message_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)