from aiogram import executor
import logging
from config import dp
from adminpanel import admin
from handlers import message_handler



logging.basicConfig(level=logging.INFO)
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
 