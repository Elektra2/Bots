#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q13_correct', state=FSM_test.Q13)
async def Q13(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q13'] = 2
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q13 = types.InlineKeyboardMarkup()
        otv = questions[13]['options']
        for i in range(len(otv)):
            if i == questions[13]['answer']:
                test_Q13.row( types.InlineKeyboardButton(otv[i], callback_data='Q14_correct'))
            else:
                test_Q13.row( types.InlineKeyboardButton(otv[i], callback_data='Q14_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[13]['photo'], caption=f"Вопрос 14/30:\n{questions[13]['question']}",
                            reply_markup=test_Q13)

@dp.callback_query_handler(text='Q13_incorrect', state=FSM_test.Q13)
async def Q13(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q13'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q13 = types.InlineKeyboardMarkup()
        otv = questions[13]['options']
        for i in range(len(otv)):
            if i == questions[13]['answer']:
                test_Q13.row( types.InlineKeyboardButton(otv[i], callback_data='Q14_correct'))
            else:
                test_Q13.row( types.InlineKeyboardButton(otv[i], callback_data='Q14_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[13]['photo'], caption=f"Вопрос 14/30:\n{questions[13]['question']}",
                            reply_markup=test_Q13)