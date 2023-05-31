#Импорты
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.test.back_to_user_menu import user_panel_back_to_main_menu1
from bd_handlers.user_profile.chage_user_score import change_score
from aiogram.dispatcher import FSMContext
from bd_handlers.user_role.create_user import create_user


#То что происходит после нажатия кнокпи "Создать пост"
@dp.callback_query_handler(text='skip_test')
async def Q1(callback_query: types.CallbackQuery, state: FSMContext):
    #Удаляем предидущее сообщение
    data = await state.get_data()
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id-1)
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id-2)
    await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='A1')
    await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/81R6j76w5Y',
                               reply_markup=user_panel_back_to_main_menu1)
    #Отправляем сообщение с клавиатурой

