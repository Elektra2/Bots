#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.show_post import FSM_change_post


#В этой функции записывается изменение название тега
@dp.message_handler(state=FSM_change_post.post_text)
async def post_tag(message: types.Message, state: FSMContext):
    #Записываем в дату название тега
    async with state.proxy() as data:
        data['post_text'] = str(message.text)
        #Переходим к следующему состоянию
        await FSM_change_post.next()
        #Отправляем сообщение
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Новое имя записи: {data['post_name']}\n"
                               f"Новый текст запсис: {data['post_text']}\n"
                               f"Статус сочинения: {data['post_list']['writing']}\n"
                               f"Введите новый статус 1 или 0:\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)