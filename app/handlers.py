import gspread
from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from oauth2client.service_account import ServiceAccountCredentials
from config import SPREADSHEET_ID

import app.keyboards as kb

router = Router()

# Установка доступа к Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Открытие Google Таблицы по ее идентификатору
spreadsheet = client.open_by_key(SPREADSHEET_ID)
sheet = spreadsheet.worksheet('Delegates')


@router.message(CommandStart())
async def command_start_handler(message: Message):
    will_join = checkup_user(message.from_user)
    print(message.from_user.full_name)
    print(message.from_user.username)
    print(message.from_user.id)
    if will_join:
        await message.answer(f"Вы отмечены, {message.from_user.full_name}!")
    else:
        await message.answer(f"Бот не нашел вас в списке, напишите администратору {message.from_user.full_name}!")


@router.message(Command('help'))
async def command_start_handler(message: Message):
    await message.answer(f"Напишите /start что бы отметить посещение форума")


def checkup_user(user):
    try:
        cell = sheet.find(user.username, in_column=2)
        if cell is not None:
            sheet.update_cell(cell.row, 3, user.id)
            sheet.update_cell(cell.row, 4, 'Y')
            return True
        else:
            return False
    except Exception as e:
        print(e)


# @router.callback_query(F.data == 'it1')
# async def callback_it(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("IT направление")
#     await add_to_google_sheet_way(f"{user_id}", "IT", 5)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'it2')
# async def callback_it(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("IT направление")
#     await add_to_google_sheet_way(f"{user_id}", "IT", 6)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'it3')
# async def callback_it(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("IT направление")
#     await add_to_google_sheet_way(f"{user_id}", "IT", 7)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'digital1')
# async def callback_digital(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("Digital направление")
#     await add_to_google_sheet_way(f"{user_id}", "Digital", 5)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'digital2')
# async def callback_digital(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("Digital направление")
#     await add_to_google_sheet_way(f"{user_id}", "Digital", 6)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'digital3')
# async def callback_digital(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("Digital направление")
#     await add_to_google_sheet_way(f"{user_id}", "Digital", 7)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'notbee1')
# async def callback_digital(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("Всегда ждем!")
#     await add_to_google_sheet_way(f"{user_id}", "N", 5)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'notbee2')
# async def callback_digital(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("Всегда ждем!")
#     await add_to_google_sheet_way(f"{user_id}", "N", 6)
#     await query.message.delete_reply_markup()
#
#
# @router.callback_query(F.data == 'notbee3')
# async def callback_digital(query: types.CallbackQuery):
#     user_id = query.from_user.id
#     await query.message.answer("Всегда ждем!")
#     await add_to_google_sheet_way(f"{user_id}", "N", 7)
#     await query.message.delete_reply_markup()


async def add_to_google_sheet_way(user_id: str, choice: str, col: int):
    cell = sheet.find(user_id, in_column=3)
    if cell is not None:
        sheet.update_cell(cell.row, col, choice)


def get_delegates():
    column_values = sheet.col_values(3)
    if column_values is not None:
        ids = column_values[1:]
        return ids
    else:
        return False


# @router.message(Command('choose1bee'))
# async def command_choose1_handler(message: Message):
#     print(message.from_user.full_name)
#     print(message.from_user.username)
#     print(message.from_user.id)
#     del_ids = get_delegates()
#     if del_ids is not False:
#         for del_id in del_ids:
#             await message.bot.send_message(chat_id=del_id, text="Какое вы выбираете направление?",
#                                            reply_markup=kb.choose_way_1)
#
#
# @router.message(Command('choose2bee'))
# async def command_choose1_handler(message: Message):
#     print(message.from_user.full_name)
#     print(message.from_user.username)
#     print(message.from_user.id)
#     del_ids = get_delegates()
#     if del_ids is not False:
#         for del_id in del_ids:
#             await message.bot.send_message(chat_id=del_id, text="Какое вы выбираете направление?",
#                                            reply_markup=kb.choose_way_2)
#
#
# @router.message(Command('choose3bee'))
# async def command_choose1_handler(message: Message):
#     print(message.from_user.full_name)
#     print(message.from_user.username)
#     print(message.from_user.id)
#     del_ids = get_delegates()
#     if del_ids is not False:
#         for del_id in del_ids:
#             await message.bot.send_message(chat_id=del_id, text="Какое вы выбираете направление?",
#                                            reply_markup=kb.choose_way_3)


# F - Фильтр
@router.message(F.text == 'test0704')
async def che_tam(message: Message):
    await message.answer(f"Ниче")
