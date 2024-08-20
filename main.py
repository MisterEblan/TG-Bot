import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


from config import BOT_TOKEN


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    
@dp.message()
async def reversedEcho(message: types.Message):
    print(message.text)
    reply = message.text [::-1]
    await message.answer(reply)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())