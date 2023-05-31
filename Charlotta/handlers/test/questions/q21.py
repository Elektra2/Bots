#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q21_correct', state=FSM_test.Q21)
async def Q21(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q21'] = 3
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q21 = types.InlineKeyboardMarkup()
        otv = questions[21]['options']
        for i in range(len(otv)):
            if i == questions[21]['answer']:
                test_Q21.row( types.InlineKeyboardButton(otv[i], callback_data='Q22_correct'))
            else:
                test_Q21.row( types.InlineKeyboardButton(otv[i], callback_data='Q22_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[21]['photo'], caption=f"Вопрос 22/30:\n{questions[21]['question']}",
                            reply_markup=test_Q21)

@dp.callback_query_handler(text='Q21_incorrect', state=FSM_test.Q21)
async def Q21(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q21'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q21 = types.InlineKeyboardMarkup()
        otv = questions[21]['options']
        for i in range(len(otv)):
            if i == questions[21]['answer']:
                test_Q21.row( types.InlineKeyboardButton(otv[i], callback_data='Q22_correct'))
            else:
                test_Q21.row( types.InlineKeyboardButton(otv[i], callback_data='Q22_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[21]['photo'], caption=f"Вопрос 22/30:\n{questions[21]['question']}",
                            reply_markup=test_Q21)