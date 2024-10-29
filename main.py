#token = 6415606396:AAGnNqE7pRM4KAmbGpnfZRdq9yWloTEknu0
from aiogram import Bot, Dispatcher, F
import asyncio
from handlers import router




async def main():
    bot = Bot(token='6415606396:AAGnNqE7pRM4KAmbGpnfZRdq9yWloTEknu0')
    disp = Dispatcher()
    disp.include_router(router)
    await disp.start_polling(bot)
    


if __name__ == '__main__':  
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("end")