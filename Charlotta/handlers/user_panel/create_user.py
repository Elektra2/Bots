from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from bd_handlers.user_role.create_user import create_user
from bd_handlers.user_role.check_user_role import check_bd_user_role
from keyboards.user_panel.test import test

class FSM_create_user_role_user(StatesGroup):
    user_id = State()
    user_name = State()

@dp.callback_query_handler(text='accept',state="*")
async def accept_tules(callback_query: types.CallbackQuery,state: FSMContext):
    message_id=callback_query.message.message_id
    for i in range(12):
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=message_id-i)
    #Отправляем сообщение с клавиатурой
    await FSM_create_user_role_user.user_id.set()
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Благодарим вас за принятие наших правил. Давайте познакомимся поближе, как мне можно к вам обращаться?",)

@dp.callback_query_handler(text='not_accpet',state="*")
async def accept_tules(callback_query: types.CallbackQuery, state: FSMContext):
    message_id=callback_query.message.message_id
    for i in range(12):
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=message_id-i)
    #Отправляем сообщение с клавиатурой
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Извините, вы должны принять правила Шарлотты, чтобы продолжить!",)
    
@dp.message_handler(state=FSM_create_user_role_user.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
        data['user_name'] = message.text
        await state.finish()
            #Вызываем bd_handler
            #Присылаем сообщение
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
        await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Рада с вами познакомиться {data['user_name']}")
        await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Добро пожаловать! Начать обучение легко - просто выберите одну из двух подписок: бесплатную Basic или с дополнительными возможностями Plus. Более подробную информацию о подписках вы можете узнать позже в главном меню.")
        await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Теперь вы можете пройти тест, который поможет мне создать для вас наиболее подходящую программу обучения. Если вы предпочитаете начать обучение с нашей минимальной программы уровня - А1, нажмите на кнопку \"Пропустить тест\"!",
                                       reply_markup=test)
