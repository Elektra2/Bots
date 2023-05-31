#Импорты
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.test.question_dic import questions



class FSM_test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()
    Q11 = State()
    Q12 = State()
    Q13 = State()
    Q14 = State()
    Q15 = State()
    Q16 = State()
    Q17 = State()
    Q18 = State()
    Q19 = State()
    Q20 = State()
    Q21 = State()
    Q22 = State()
    Q23 = State()
    Q24 = State()
    Q25 = State()
    Q26 = State()
    Q27 = State()
    Q28 = State()
    Q29 = State()
    Q30 = State()
    



#То что происходит после нажатия кнокпи "Создать пост"
@dp.callback_query_handler(text='start_test')
async def Q1(callback_query: types.CallbackQuery):
    await FSM_test.Q1.set()
    #Удаляем предидущее сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id-1)
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id-2)
    #Отправляем сообщение с клавиатурой
    test_first = types.InlineKeyboardMarkup()
    otv = questions[0]['options']
    for i in range(len(otv)):
        if i == questions[0]['answer']:
            test_first.row( types.InlineKeyboardButton(otv[i], callback_data='first_correct'))
        else:
            test_first.row( types.InlineKeyboardButton(otv[i], callback_data='first_incorrect'))
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[0]['photo'], caption=f"Вопрос 1/30:\n{questions[0]['question']}",
                           reply_markup=test_first)
