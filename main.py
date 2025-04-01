from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
import asyncio

bot_token = "6687031708:AAExe7Dq5xv4Z2F4j_OeonKcuqcWOMIo6NQ"
bot = Bot(token=bot_token)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("Привет! Это тестовый бот.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
