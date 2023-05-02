from aiogram import types
from dispatcher import DP, GPT


@DP.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi!\nI'm a bot developed as a test assignment for Chatfuel. My author is Maxim Frolov. "
                         "You can ask me about purchasing a trial subscription.")


@DP.message_handler()
async def echo(message: types.Message):
    await message.answer(GPT.response_from_gpt(message.text))
