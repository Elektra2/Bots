#Импорты
from keyboards.post_list.post_lvl import show_post_lvl
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup

#машина состояний
class FSM_create_test(StatesGroup):
    post_list = State()
    cur_list = State()
    post_name = State()
    post_test = State()
    questions = State()
    question_id = State()


#То что происходит после нажатия кнокпи "Изменить пост"
@dp.callback_query_handler(text='create_test')
async def admin_panel_change_post_callback(callback_query: types.CallbackQuery):
    await FSM_create_test.post_list.set()
    #Удаляем предидущее сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Выберите уровень записти",
                               reply_markup=show_post_lvl)