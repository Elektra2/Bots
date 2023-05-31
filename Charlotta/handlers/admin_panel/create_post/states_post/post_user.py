#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_post.create_post import FSM_create_post
from aiogram.types import InputMediaPhoto


#В этой функции записывается описание
@dp.message_handler(state=FSM_create_post.post_uesr)
async def post_disc(message: types.Message, state: FSMContext):
    #Записываем в дату описание
    async with state.proxy() as data:
        disc = message.text
        data['post_user'] = disc
        #Переходим к следующему состоянию
        await FSM_create_post.next()
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
        #Отправляем сообщение
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"ID пользователя: {message.from_user.id}\n"
                               f"Название: {data['post_name']}\n"
                               f"Для пользователя: {data['post_user']}\n"
                               f"Введите текст записи:\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)