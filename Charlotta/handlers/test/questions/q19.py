#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q19_correct', state=FSM_test.Q19)
async def Q19(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q19'] = 3
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q19 = types.InlineKeyboardMarkup()
        otv = questions[19]['options']
        for i in range(len(otv)):
            if i == questions[19]['answer']:
                test_Q19.row( types.InlineKeyboardButton(otv[i], callback_data='Q20_correct'))
            else:
                test_Q19.row( types.InlineKeyboardButton(otv[i], callback_data='Q20_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[19]['photo'], caption=f"Вопрос 20/30:\n{questions[19]['question']}",
                            reply_markup=test_Q19)

@dp.callback_query_handler(text='Q19_incorrect', state=FSM_test.Q19)
async def Q19(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q19'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q19 = types.InlineKeyboardMarkup()
        otv = questions[19]['options']
        for i in range(len(otv)):
            if i == questions[19]['answer']:
                test_Q19.row( types.InlineKeyboardButton(otv[i], callback_data='Q20_correct'))
            else:
                test_Q19.row( types.InlineKeyboardButton(otv[i], callback_data='Q20_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[19]['photo'], caption=f"Вопрос 20/30:\n{questions[19]['question']}",
                            reply_markup=test_Q19)