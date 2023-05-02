import logging
from aiogram import Bot, Dispatcher
import config
from utils.gpt_handler import GPT3interface


logging.basicConfig(level=logging.INFO)

if not config.BOT_TOKEN:
    exit("No token provided")

GPT = GPT3interface()
BOT = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
DP = Dispatcher(BOT)
