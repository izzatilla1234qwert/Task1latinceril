import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from transliterate import to_cyrillic, to_latin

API_TOKEN = '7264801834:AAEm0auzyylOIMMqLFZKeCaSfpryRUVM7YA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

def transliterate_text(text):
    if text and all('a' <= char.lower() <= 'z' or char.isspace() for char in text):
        return to_cyrillic(text)
    else:
        return to_latin(text)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Matnni yuboring, men uni lotincha-kirillcha yoki kirillcha-lotincha o'giraman.")

@dp.message_handler()
async def transliterate_message(message: types.Message):
    original_text = message.text
    transliterated_text = transliterate_text(original_text)
    await message.reply(transliterated_text, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
