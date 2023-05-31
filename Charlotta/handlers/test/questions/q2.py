#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='second_correct', state=FSM_test.Q2)
async def Q3(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q2'] = 1
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q3 = types.InlineKeyboardMarkup()
        otv = questions[2]['options']
        for i in range(len(otv)):
            if i == questions[2]['answer']:
                test_Q3.row( types.InlineKeyboardButton(otv[i], callback_data='Q3_correct'))
            else:
                test_Q3.row( types.InlineKeyboardButton(otv[i], callback_data='Q3_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[2]['photo'], caption=f"Вопрос 3/30:\n{questions[2]['question']}",
                            reply_markup=test_Q3)

@dp.callback_query_handler(text='second_incorrect', state=FSM_test.Q2)
async def Q3(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q2'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q3 = types.InlineKeyboardMarkup()
        otv = questions[2]['options']
        for i in range(len(otv)):
            if i == questions[2]['answer']:
                test_Q3.row( types.InlineKeyboardButton(otv[i], callback_data='Q3_correct'))
            else:
                test_Q3.row( types.InlineKeyboardButton(otv[i], callback_data='Q3_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[2]['photo'], caption=f"Вопрос 3/30:\n{questions[2]['question']}",
                            reply_markup=test_Q3)