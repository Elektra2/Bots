#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q28_correct', state=FSM_test.Q28)
async def Q28(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q28'] = 1
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q28 = types.InlineKeyboardMarkup()
        otv = questions[28]['options']
        for i in range(len(otv)):
            if i == questions[28]['answer']:
                test_Q28.row( types.InlineKeyboardButton(otv[i], callback_data='Q29_correct'))
            else:
                test_Q28.row( types.InlineKeyboardButton(otv[i], callback_data='Q29_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[28]['photo'], caption=f"Вопрос 29/30:\n{questions[28]['question']}",
                            reply_markup=test_Q28)

@dp.callback_query_handler(text='Q28_incorrect', state=FSM_test.Q28)
async def Q28(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q28'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q28 = types.InlineKeyboardMarkup()
        otv = questions[28]['options']
        for i in range(len(otv)):
            if i == questions[28]['answer']:
                test_Q28.row( types.InlineKeyboardButton(otv[i], callback_data='Q29_correct'))
            else:
                test_Q28.row( types.InlineKeyboardButton(otv[i], callback_data='Q29_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[28]['photo'], caption=f"Вопрос 29/30:\n{questions[28]['question']}",
                            reply_markup=test_Q28)