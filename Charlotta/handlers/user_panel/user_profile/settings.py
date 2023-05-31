#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel.settings import settings_menu
from bd_handlers.user_profile.chage_user_name import change_name
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bd_handlers.materials.get_user import get_user


class FSM_settings(StatesGroup):
    settings = State()
    name = State()
    sub = State()

#То что происходит после нажатия кнокпи "Выйти в главное меню"
@dp.callback_query_handler(text='settings', state='*')
async def PROFILE(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSM_settings.settings.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Вам доступны опции для изменения имени в этом меню. Если возникнут вопросы, я всегда к вашим услугам!",
                               reply_markup=settings_menu)

@dp.callback_query_handler(text='chage_name', state=FSM_settings.settings)
async def username(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_settings.next()
    back = types.InlineKeyboardMarkup().row(types.InlineKeyboardButton('Назад',callback_data='settings'))
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Введите новое имя пользователя:",
                               reply_markup=back)

@dp.message_handler(state=FSM_settings.name)
async def post_name(message: types.Message, state: FSMContext):
    back = types.InlineKeyboardMarkup().row(types.InlineKeyboardButton('Назад',callback_data='settings'))
    await change_name(user_id=message.from_user.id,score=message.text)
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Имя пользователя изменено на {message.text}",
                           reply_markup=back)
    
@dp.callback_query_handler(text='rest_test', state=FSM_settings.sub)
async def username(callback_query: types.CallbackQuery, state: FSMContext):
    user = await get_user(callback_query.from_user.id)