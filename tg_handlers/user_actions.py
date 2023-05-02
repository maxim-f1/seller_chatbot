from aiogram import types
from dispatcher import DP, GPT


@DP.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi!\n"
                         "I'm a bot developed as a test assignment for Chatfuel.\n"
                         "My author is Frolov Maxim: @WATYNeed.\n"
                         "GitHub: https://github.com/WATUNeed/seller_chatbot\n"
                         "You can ask me about purchasing a trial subscription.")


@DP.message_handler()
async def echo_response(message: types.Message):
    answer = await message.answer('Typing...')
    await answer.edit_text(GPT.response_from_gpt(message.text))
