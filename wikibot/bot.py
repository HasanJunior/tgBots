"""
This is a echo bot.
It echoes any incoming text messages.

aiogram 2.14.3
"""

import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6881797175:AAHoAuuXvALPnHwNPbmhRtYkgZijhfVlKQ0'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.text("Bu so'rovingiz haqida ma'lumotga ega emasman")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)