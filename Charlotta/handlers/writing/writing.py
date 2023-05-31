#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.writing.writing_menu import writing_menu
from aiogram.dispatcher import FSMContext
from bd_handlers.user_role.get_user_name import get_user_name
from aiogram.dispatcher.filters.state import State, StatesGroup
    
class FSM_show_writing(StatesGroup):
    user = State()
    cur_list = State()
    post = State()
    essay = State()

#То что происходит после нажатия кнокпи "Выйти в главное меню"
@dp.callback_query_handler(text='writing',state='*')
async def admin_panel_main_menu_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    #Удаляем предидущее сообщение
    await FSM_show_writing.user.set()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    user_id = int(callback_query.from_user.id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Здесь вы можете написать эссе и посмотреть результаты проверки👩‍🏫",
                               reply_markup=writing_menu)