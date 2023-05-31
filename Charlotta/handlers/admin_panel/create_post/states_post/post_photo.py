from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_post.create_post import FSM_create_post


#В этой функции записывается тег
@dp.message_handler(state=FSM_create_post.post_photo)
async def load_user_id(message: types.Message, state: FSMContext):
    #Записываем в дату тег
    async with state.proxy() as data:
        data['post_photo'] = message.text
        #Переходим к следующему состоянию
        await FSM_create_post.next()
        #Отправляем сообщение
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"ID пользователя: {message.from_user.id}\n"
                               f"Название: {data['post_name']}\n"
                               f"Для пользователя: {data['post_user']}\n"
                               f"Текст: {data['post_text']}\n"
                               f"Pdf: {data['post_photo']}\n"
                               f"Введите 1 если надо писать сочинение 0 если не надо:\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)