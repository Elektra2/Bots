#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q22_correct', state=FSM_test.Q22)
async def Q22(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q22'] = 4
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q22 = types.InlineKeyboardMarkup()
        otv = questions[22]['options']
        for i in range(len(otv)):
            if i == questions[22]['answer']:
                test_Q22.row( types.InlineKeyboardButton(otv[i], callback_data='Q23_correct'))
            else:
                test_Q22.row( types.InlineKeyboardButton(otv[i], callback_data='Q23_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[22]['photo'], caption=f"Вопрос 23/30:\n{questions[22]['question']}",
                            reply_markup=test_Q22)

@dp.callback_query_handler(text='Q22_incorrect', state=FSM_test.Q22)
async def Q22(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q22'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q22 = types.InlineKeyboardMarkup()
        otv = questions[22]['options']
        for i in range(len(otv)):
            if i == questions[22]['answer']:
                test_Q22.row( types.InlineKeyboardButton(otv[i], callback_data='Q23_correct'))
            else:
                test_Q22.row( types.InlineKeyboardButton(otv[i], callback_data='Q23_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[22]['photo'], caption=f"Вопрос 23/30:\n{questions[22]['question']}",
                            reply_markup=test_Q22)