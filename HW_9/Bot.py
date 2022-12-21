import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import user

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher

bot = Bot(token='5978519714:AAH15-fPqBSvykawKS1ebuo4KaiiPVr5yM8')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply(f"Здравствуйте, {message.reply_to_message.from_user.first_name}\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:

    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
