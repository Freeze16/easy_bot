import asyncio

from aiogram import Bot, Dispatcher

from bot.config import load_config


async def main():
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    await dp.start_polling(bot)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")
