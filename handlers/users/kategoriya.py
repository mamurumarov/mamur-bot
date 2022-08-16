from cgitb import text
from aiogram import types
from keyboards.default.cats import cats_keyboard
from loader import dp, db
from states.holat import Kafe
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message_handler(text="🛍 Buyurtma berish")
async def bot_echo(message: types.Message):
    await message.answer("Ovqatni tanlang", reply_markup=cats_keyboard)
    await Kafe.cats.set()


@dp.message_handler(state=Kafe.cats)
async def get_sub_cats(message: types.Message):
    cat = message.text
    sub_cat_id = db.select_sub_cat_id(name=cat)[0]
    sub_cats = db.select_all_sub_cats(cat_id=sub_cat_id)
    if len(sub_cats) == 0:
        await message.answer("Malumotlar topilmadi")
    else:
        markub = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in sub_cats:
            markub.insert(KeyboardButton(text=i[0]))
        await message.answer("tanlang", reply_markup=markub)
        await Kafe.next()
