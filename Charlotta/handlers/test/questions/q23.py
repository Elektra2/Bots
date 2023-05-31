#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q23_correct', state=FSM_test.Q23)
async def Q23(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q23'] = 4
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q23 = types.InlineKeyboardMarkup()
        otv = questions[23]['options']
        for i in range(len(otv)):
            if i == questions[23]['answer']:
                test_Q23.row( types.InlineKeyboardButton(otv[i], callback_data='Q24_correct'))
            else:
                test_Q23.row( types.InlineKeyboardButton(otv[i], callback_data='Q24_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[23]['photo'], caption=f"Вопрос 24/30:\n{questions[23]['question']}",
                            reply_markup=test_Q23)

@dp.callback_query_handler(text='Q23_incorrect', state=FSM_test.Q23)
async def Q23(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q23'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q23 = types.InlineKeyboardMarkup()
        otv = questions[23]['options']
        for i in range(len(otv)):
            if i == questions[23]['answer']:
                test_Q23.row( types.InlineKeyboardButton(otv[i], callback_data='Q24_correct'))
            else:
                test_Q23.row( types.InlineKeyboardButton(otv[i], callback_data='Q24_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[23]['photo'], caption=f"Вопрос 24/30:\n{questions[23]['question']}",
                            reply_markup=test_Q23)