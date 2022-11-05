from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5625555312:AAGY_-Ik7OnzE2Yg0E1YmaAIyEgzrqVCCa0'
bot_id = API_TOKEN.split(':')[0]
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
admins = [5356014595]