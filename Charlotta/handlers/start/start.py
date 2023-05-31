#Импорты
from aiogram import types
from config.bot_config import dp, bot, logging
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from keyboards.cm_keyboard_main_menu import cm_keyboard_main_menu
from keyboards.accept_rules import accept_rules_menu
from keyboards.user_panel.user_main_menu import user_main_menu
from bd_handlers.user_role.check_user_role import check_bd_user_role
from bd_handlers.user_role.get_user_name import get_user_name
from aiogram.types import InputMediaPhoto
import time
from aiogram.dispatcher import FSMContext

#Хендлер реагирует на комманду старт.
@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    user_id = int(message.from_user.id)
    check_user_role = await check_bd_user_role(user_id=user_id)
    if check_user_role == 'admin':
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}",
                               reply_markup=admin_panel_keyboard_main_menu)
    #Если роль пользователя контент менеджер то
    elif check_user_role == 'cm':
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}",
                               reply_markup=cm_keyboard_main_menu)
    elif check_user_role != None and check_user_role != "None":
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Привет, {await get_user_name(user_id=user_id)}",
                               reply_markup=user_main_menu)
    #Если нет роли пользователя то
    else:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        user_full_name = message.from_user.full_name
        logging.info(f'{user_id} {user_full_name} {time.asctime()}')
        await message.answer(f"Hi and Welcome! Я - Шарлотта, ваш персональный ассистент в Английском языке.")
        pictures = [
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/Ndd4kSWBt1", caption="Picture 1"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/p402Q133Vi", caption="Picture 2"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/71774Md9w5", caption="Picture 3"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/CtUc14w3aa", caption="Picture 4"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/1D5uw1Bu5w", caption="Picture 5"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/95F0J24742", caption="Picture 6"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/65623V7XS4", caption="Picture 7"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/1oq2Fy7200", caption="Picture 8"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/ijdjdywvoq", caption="Picture 9"), ]
        await bot.send_media_group(chat_id=user_id, 
                                   media=pictures,)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Чтобы продолжить наше знакомство, пожалуйста, примите правила использования чат-бота Шарлотта!",
                               reply_markup=accept_rules_menu)

