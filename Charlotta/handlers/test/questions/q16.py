#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q16_correct', state=FSM_test.Q16)
async def Q16(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q16'] = 1
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q16 = types.InlineKeyboardMarkup()
        otv = questions[16]['options']
        for i in range(len(otv)):
            if i == questions[16]['answer']:
                test_Q16.row( types.InlineKeyboardButton(otv[i], callback_data='Q17_correct'))
            else:
                test_Q16.row( types.InlineKeyboardButton(otv[i], callback_data='Q17_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[16]['photo'], caption=f"Вопрос 17/30:\n{questions[16]['question']}",
                            reply_markup=test_Q16)

@dp.callback_query_handler(text='Q16_incorrect', state=FSM_test.Q16)
async def Q16(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q16'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q16 = types.InlineKeyboardMarkup()
        otv = questions[16]['options']
        for i in range(len(otv)):
            if i == questions[16]['answer']:
                test_Q16.row( types.InlineKeyboardButton(otv[i], callback_data='Q17_correct'))
            else:
                test_Q16.row( types.InlineKeyboardButton(otv[i], callback_data='Q17_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[16]['photo'], caption=f"Вопрос 17/30:\n{questions[16]['question']}",
                            reply_markup=test_Q16)