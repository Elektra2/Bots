#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel.profile_menu import profile_menu
from bd_handlers.user_profile.profile import bd_profile
from aiogram.dispatcher import FSMContext
from handlers.user_panel.user_profile.subscribe import FSM_back
from handlers.user_panel.user_profile.subscribe import buy

#То что происходит после нажатия кнокпи "Выйти в главное меню"
@dp.callback_query_handler(text='show_profile', state='*')
async def PROFILE(callback_query: types.CallbackQuery, state: FSMContext):
    curr_state = await state.get_state()
    user = await bd_profile(callback_query.from_user.id)
    role = user['user_role']
    #Ничего не делать, если состояния нет
    if curr_state is None:
        await state.finish()
        #Удаляем предидущее сообщение
        sub = ''
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Добро пожаловать в ваш личный кабинет, {user['user_name']}\n"
                               f"Ваш рекомендуемый уровень материалов - {user['score']}\n"
                               f"Ваша подписка - {role.capitalize()}",
                               reply_markup=profile_menu)
        
    elif curr_state is not None:
        await state.finish()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Добро пожаловать в ваш личный кабинет, {user['user_name']}\n"
                               f"Ваш рекомендуемый уровень материалов - {user['score']}\n"
                               f"Ваша подписка - {role}",
                               reply_markup=profile_menu)
        
@dp.callback_query_handler(text='show_profile1', state=FSM_back.back)
async def PROFILE(callback_query: types.CallbackQuery, state: FSMContext):
    curr_state = await state.get_state()
    user = await bd_profile(callback_query.from_user.id)
    role = user['user_role']
    #Ничего не делать, если состояния нет
    if curr_state is None:
        await state.finish()
        #Удаляем предидущее сообщение
        sub = ''
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id-2)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id-1)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Добро пожаловать в ваш личный кабинет, {user['user_name']}\n"
                               f"Ваш рекомендуемый уровень материалов - {user['score']}\n"
                               f"Ваша подписка - {role.capitalize()}",
                               reply_markup=profile_menu)
        
    elif curr_state is not None:
        await state.finish()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id-2)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id-1)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Добро пожаловать в ваш личный кабинет, {user['user_name']}\n"
                               f"Ваш рекомендуемый уровень материалов - {user['score']}\n"
                               f"Ваша подписка - {role.capitalize()}",
                               reply_markup=profile_menu)
    
@dp.callback_query_handler(text='show_profile2', state=FSM_back.back)
async def PROFILE(callback_query: types.CallbackQuery, state: FSMContext):
    curr_state = await state.get_state()
    user = await bd_profile(callback_query.from_user.id)
    role = user['user_role']
    #Ничего не делать, если состояния нет
    if curr_state is None:
        await state.finish()
        #Удаляем предидущее сообщение
        sub = ''

        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Добро пожаловать в ваш личный кабинет, {user['user_name']}\n"
                               f"Ваш рекомендуемый уровень материалов - {user['score']}\n"
                               f"Ваша подписка - {role.capitalize()}",
                               reply_markup=profile_menu)
        
    elif curr_state is not None:
        await state.finish()
        #Удаляем предидущее сообщение
        #Отправляем сообщение с клавиатурой
        data = await state.get_data()

        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Добро пожаловать в ваш личный кабинет, {user['user_name']}\n"
                               f"Ваш рекомендуемый уровень материалов - {user['score']}\n"
                               f"Ваша подписка - {role.capitalize()}",
                               reply_markup=profile_menu)