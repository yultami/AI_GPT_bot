from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
         InlineKeyboardButton(text="Начать чат", callback_data="create_chat")]])