import time

from aiogram import *

a=input("Введите токен") 
s=input("Text message ") 
bot = Bot(a)
dp = Dispatcher(bot)


@dp.message_handler(commands=["flood"])
async def flood(message: types.Message):
    try:
        message_to_forward = await message.answer(s)
        for i in range(int(message.text.replace("/flood ", ""))):
            await message_to_forward.forward(message.chat.id, False)
    except:
        await message.reply("Error")
        time.sleep(10)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
