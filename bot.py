import time

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ParseMode, ChatType

from config import TOKEN

import weather_api

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def welcome(msg: Message):
    if msg.chat.type == ChatType.PRIVATE:
        await bot.send_message(msg.chat.id, "Hello friend. Could you send me the name of the city ?")
        await bot.send_message(msg.chat.id, "For exaple: /search <b>Toshkent</b>", parse_mode=ParseMode.HTML)


@dp.message_handler(commands='search')
async def a(msg: Message):
    text = msg.text.split(' ')
    print(text)
    mes = await bot.send_message(msg.chat.id, '⏳')
    time.sleep(3)
    try:
        req = weather_api.req(text[-1])
        ans = f'''temperature: {req["main"]['temp']}
temperature_max: {req['main']['temp_max']}
wind-speed: {req['wind']['speed']}
        '''

        await bot.send_message(msg.chat.id, ans)

    except Exception:
        await bot.delete_message(msg.chat.id, message_id=mes.message_id)
        await bot.send_message(msg.chat.id, 'You sent the request incorrectly')
        await bot.send_message(msg.chat.id, 'For exaple: /search Toshkent \n/search London')




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)