#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q5_correct', state=FSM_test.Q5)
async def Q6(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q5'] = 1
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q5 = types.InlineKeyboardMarkup()
        otv = questions[5]['options']
        for i in range(len(otv)):
            if i == questions[5]['answer']:
                test_Q5.row( types.InlineKeyboardButton(otv[i], callback_data='Q6_correct'))
            else:
                test_Q5.row( types.InlineKeyboardButton(otv[i], callback_data='Q6_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[5]['photo'], caption=f"Вопрос 6/30:\n{questions[5]['question']}",
                            reply_markup=test_Q5)

@dp.callback_query_handler(text='Q5_incorrect', state=FSM_test.Q5)
async def Q6(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q5'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q5 = types.InlineKeyboardMarkup()
        otv = questions[5]['options']
        for i in range(len(otv)):
            if i == questions[5]['answer']:
                test_Q5.row( types.InlineKeyboardButton(otv[i], callback_data='Q6_correct'))
            else:
                test_Q5.row( types.InlineKeyboardButton(otv[i], callback_data='Q6_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[5]['photo'], caption=f"Вопрос 6/30:\n{questions[5]['question']}",
                            reply_markup=test_Q5)