from aiogram import executor
from dispatcher import DP
import tg_handlers


if __name__ == "__main__":
    executor.start_polling(DP, skip_updates=True)
