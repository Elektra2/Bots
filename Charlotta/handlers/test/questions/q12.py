#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q12_correct', state=FSM_test.Q12)
async def Q12(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q12'] = 3
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q12 = types.InlineKeyboardMarkup()
        otv = questions[12]['options']
        for i in range(len(otv)):
            if i == questions[12]['answer']:
                test_Q12.row( types.InlineKeyboardButton(otv[i], callback_data='Q13_correct'))
            else:
                test_Q12.row( types.InlineKeyboardButton(otv[i], callback_data='Q13_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[12]['photo'], caption=f"Вопрос 13/30:\n{questions[12]['question']}",
                            reply_markup=test_Q12)

@dp.callback_query_handler(text='Q12_incorrect', state=FSM_test.Q12)
async def Q12(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q12'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_Q12 = types.InlineKeyboardMarkup()
        otv = questions[12]['options']
        for i in range(len(otv)):
            if i == questions[12]['answer']:
                test_Q12.row( types.InlineKeyboardButton(otv[i], callback_data='Q13_correct'))
            else:
                test_Q12.row( types.InlineKeyboardButton(otv[i], callback_data='Q13_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[12]['photo'], caption=f"Вопрос 13/30:\n{questions[12]['question']}",
                            reply_markup=test_Q12)