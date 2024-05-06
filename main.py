import asyncio
import logging
import sys

import gspread
from aiogram import Bot, Dispatcher
from oauth2client.service_account import ServiceAccountCredentials

from app.handlers import router
from config import TOKEN


async def main() -> None:
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

# # Простая имитация базы данных для хранения информации о том, кому уже было отправлено приветствие
# sent_hello_to = set()
#
#
# @dp.message(Command("obed"))
# async def cmd_obed(message: types.Message):
#     global sent_hello_to
#
#     for id in sent_hello_to:
#         await bot.send_message(id, "Выберите трек:", reply_markup=keyboards.keyboardItDigital)
#
# @dp.callback_query_handler(func=lambda c: c.data == 'obed')
# async def process_callback(callback_query: types.CallbackQuery):
#     global sent_hello_to
#
#     for id in sent_hello_to:
#         if callback_query.data == 'it':
#             await bot.answer_callback_query(callback_query.id)
#             await bot.send_message(id, "Вы выбрали трек IT")
#         elif callback_query.data == 'digital':
#             await bot.answer_callback_query(callback_query.id)
#             await bot.send_message(id, "Вы выбрали трек Digital")
#
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     global sent_hello_to
#     # Добавляем ID пользователя в список тех, кому было отправлено приветствие
#     sent_hello_to.add(message.from_user.id)
#     # Отправляем приветственное сообщение
#
#     user_channel_status = await bot.get_chat_member(chat_id="-1001970983421", user_id=message.from_user.id)
#     print(message.from_user.username)
#     print(user_channel_status)
#     if user_channel_status.status != "left":
#         await message.answer("""```
#  _
# | |
# | |__   ___  ___
# | '_ \\ / _ \\/ _ \\
# | |_) |  __/  __/
# |_.__/ \\___|\\___|
#         ```""", parse_mode='Markdown')
#         await add_to_sheet(message.from_user)
#         pass
#     else:
#         await message.answer("""```
#  _ __   ___
# | '_ \\ / _ \\
# | | | | (_) |
# |_| |_|\\___/
#         ```""", parse_mode='Markdown')
#
# #Код отправки сообщения в заданное время
#     # if user_channel_status.status != "left":
#     #     while True:
#     #         await asyncio.sleep(1)
#     #         now = datetime.datetime.now()
#     #         current_time = now.strftime("%H:%M")
#     #         if current_time == '04:20':
#     #             await bot.send_message(message.chat.id, f'"Это сообщение отправлено в {current_time}"')
#
#
# # async def send_way():
# #     global sent_hello_to
# #
# #     # Получаем текущее время
# #     current_time = datetime.datetime.now().time()
# #
# #     # Отправляем приветственное сообщение всем пользователям, которым еще не было отправлено сегодня
# #     for user_id in sent_hello_to:
# #         await bot.send_message(chat_id=user_id, text='Привет!')
# #
# #         # Добавляем текущую дату в список отправленных
# #     sent_hello_to.add(datetime.date.today())
#
#
#
# # schedule.every().day.at("3:44").do(send_way)
#
# # await asyncio.sleep(60)
# async def main():
#     await dp.start_polling(bot)
#     # while True:
#     #     schedule.run_pending()
#     #     time.sleep(1)
#
#
# if __name__ == "__main__":
#     print("PchelaBOT is running")
#     asyncio.run(main())
