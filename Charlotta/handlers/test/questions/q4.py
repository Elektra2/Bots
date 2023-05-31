#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q4_correct', state=FSM_test.Q4)
async def Q5(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q4'] = 1
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q4 = types.InlineKeyboardMarkup()
        otv = questions[4]['options']
        for i in range(len(otv)):
            if i == questions[3]['answer']:
                test_Q4.row( types.InlineKeyboardButton(otv[i], callback_data='Q5_correct'))
            else:
                test_Q4.row( types.InlineKeyboardButton(otv[i], callback_data='Q5_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[4]['photo'], caption=f"Вопрос 5/30:\n{questions[4]['question']}",
                            reply_markup=test_Q4)

@dp.callback_query_handler(text='Q4_incorrect', state=FSM_test.Q4)
async def Q5(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q4'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q4 = types.InlineKeyboardMarkup()
        otv = questions[4]['options']
        for i in range(len(otv)):
            if i == questions[4]['answer']:
                test_Q4.row( types.InlineKeyboardButton(otv[i], callback_data='Q5_correct'))
            else:
                test_Q4.row( types.InlineKeyboardButton(otv[i], callback_data='Q5_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[4]['photo'], caption=f"Вопрос 5/30:\n{questions[4]['question']}",
                            reply_markup=test_Q4)