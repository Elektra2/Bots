#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q29_correct', state=FSM_test.Q29)
async def Q29(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q29'] = 3
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q29 = types.InlineKeyboardMarkup()
        otv = questions[29]['options']
        for i in range(len(otv)):
            if i == questions[29]['answer']:
                test_Q29.row( types.InlineKeyboardButton(otv[i], callback_data='Q30_correct'))
            else:
                test_Q29.row( types.InlineKeyboardButton(otv[i], callback_data='Q30_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[29]['photo'], caption=f"Вопрос 30/30:\n{questions[29]['question']}",
                            reply_markup=test_Q29)

@dp.callback_query_handler(text='Q29_incorrect', state=FSM_test.Q29)
async def Q29(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q29'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q29 = types.InlineKeyboardMarkup()
        otv = questions[29]['options']
        for i in range(len(otv)):
            if i == questions[29]['answer']:
                test_Q29.row( types.InlineKeyboardButton(otv[i], callback_data='Q30_correct'))
            else:
                test_Q29.row( types.InlineKeyboardButton(otv[i], callback_data='Q30_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[29]['photo'], caption=f"Вопрос 30/30:\n{questions[29]['question']}",
                            reply_markup=test_Q29)