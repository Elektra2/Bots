#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q9_correct', state=FSM_test.Q9)
async def Q10(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q9'] = 3
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q9 = types.InlineKeyboardMarkup()
        otv = questions[9]['options']
        for i in range(len(otv)):
            if i == questions[9]['answer']:
                test_Q9.row( types.InlineKeyboardButton(otv[i], callback_data='Q10_correct'))
            else:
                test_Q9.row( types.InlineKeyboardButton(otv[i], callback_data='Q10_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[9]['photo'], caption=f"Вопрос 10/30:\n{questions[9]['question']}",
                            reply_markup=test_Q9)

@dp.callback_query_handler(text='Q9_incorrect', state=FSM_test.Q9)
async def Q9(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q9'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q9 = types.InlineKeyboardMarkup()
        otv = questions[9]['options']
        for i in range(len(otv)):
            if i == questions[9]['answer']:
                test_Q9.row( types.InlineKeyboardButton(otv[i], callback_data='Q10_correct'))
            else:
                test_Q9.row( types.InlineKeyboardButton(otv[i], callback_data='Q10_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[9]['photo'], caption=f"Вопрос 10/30:\n{questions[9]['question']}",
                            reply_markup=test_Q9)