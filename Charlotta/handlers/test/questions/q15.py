#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q15_correct', state=FSM_test.Q15)
async def Q15(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q15'] = 2
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q15 = types.InlineKeyboardMarkup()
        otv = questions[15]['options']
        for i in range(len(otv)):
            if i == questions[15]['answer']:
                test_Q15.row( types.InlineKeyboardButton(otv[i], callback_data='Q16_correct'))
            else:
                test_Q15.row( types.InlineKeyboardButton(otv[i], callback_data='Q16_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[15]['photo'], caption=f"Вопрос 16/30:\n{questions[15]['question']}",
                            reply_markup=test_Q15)

@dp.callback_query_handler(text='Q15_incorrect', state=FSM_test.Q15)
async def Q15(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q15'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q15 = types.InlineKeyboardMarkup()
        otv = questions[15]['options']
        for i in range(len(otv)):
            if i == questions[15]['answer']:
                test_Q15.row( types.InlineKeyboardButton(otv[i], callback_data='Q16_correct'))
            else:
                test_Q15.row( types.InlineKeyboardButton(otv[i], callback_data='Q16_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[15]['photo'], caption=f"Вопрос 16/30:\n{questions[15]['question']}",
                            reply_markup=test_Q15)