from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_post.create_post import FSM_create_post
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
from bd_handlers.create_post.create_post import create_post
from bd_handlers.create_post.check_user_name import check_bd_user_name
import datetime


#В этой функции отправляется запрос в БД и создается запись в канале
@dp.message_handler(state=FSM_create_post.post_lvl)
async def load_user_id(message: types.Message, state: FSMContext):
    #Записываем ссылку в дату
    async with state.proxy() as data:
        data['post_lvl'] = message.text
        #Закрываем состояние
        await state.finish()
        #вывод данных в нужных нам типах
        user_id = int(message.from_user.id)
        post_name = str(data['post_name'])
        post_text = str(data['post_text'])
        post_photo = str(data['post_photo'])
        post_lvl = str(data['post_lvl'])
        cur_date = str(datetime.datetime.now().date())
        cur_time = str(datetime.datetime.now().time().replace(microsecond=0))
        #sql функция
        user_name = await check_bd_user_name(user_id=user_id)
        #sql функция
        await create_post(post_name=post_name, post_text=post_text, post_photo=post_photo, post_lvl=post_lvl,
                          user_name=user_name, create_data=cur_date, create_time=cur_time, post_for=data['post_user'], writing=data['post_writing'])
        #Отправляем сообщение себе в бота
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"ID пользователя:\n{message.from_user.id}\n"
                               f"Название:\n{post_name}\n"
                               f"Для пользователя: {data['post_user']}\n"
                               f"Текст:\n{post_text}\n"
                               f"Pdf:\n{post_photo}\n"
                               f"Уровень сложности:\n{post_lvl}\n"
                               f"Создано:\n{user_name}\n"
                               f"Дата создания:\n{cur_date}\n"
                               f"Время создания создания:\n{cur_time}\n"
                               f"Вы успешно создали запись\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)        