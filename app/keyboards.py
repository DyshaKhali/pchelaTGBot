from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choose_way_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="IT", callback_data='it1'), InlineKeyboardButton(text="Digital", callback_data='digital1')],
    [InlineKeyboardButton(text="Не иду", callback_data='notbee1')]
])

choose_way_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="IT", callback_data='it2'), InlineKeyboardButton(text="Digital", callback_data='digital2')],
    [InlineKeyboardButton(text="Не иду", callback_data='notbee2')]
])

choose_way_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="IT", callback_data='it3'), InlineKeyboardButton(text="Digital", callback_data='digital3')],
    [InlineKeyboardButton(text="Не иду", callback_data='notbee3')]
])
