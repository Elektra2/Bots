#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.test.start_test import FSM_test


#В этой функции записывается название поста
@dp.callback_query_handler(text='first_correct', state=FSM_test.Q1)
async def Q2(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q1'] = 1
        #Переходим к следующему состоянию
        await FSM_test.next()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_second = types.InlineKeyboardMarkup()
        otv = questions[1]['options']
        for i in range(len(otv)):
            if i == questions[1]['answer']:
                test_second.row( types.InlineKeyboardButton(otv[i], callback_data='second_correct'))
            else:
                test_second.row( types.InlineKeyboardButton(otv[i], callback_data='second_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[1]['photo'], caption=f"Вопрос 2/30:\n{questions[1]['question']}",
                            reply_markup=test_second)

@dp.callback_query_handler(text='first_incorrect', state=FSM_test.Q1)
async def Q2(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q1'] = 0
        #Переходим к следующему состоянию
        await FSM_test.next()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        test_second = types.InlineKeyboardMarkup()
        otv = questions[1]['options']
        for i in range(len(otv)):
            if i == questions[1]['answer']:
                test_second.row( types.InlineKeyboardButton(otv[i], callback_data='second_correct'))
            else:
                test_second.row( types.InlineKeyboardButton(otv[i], callback_data='second_incorrect'))
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=questions[1]['photo'], caption=f"Вопрос 2/30:\n{questions[1]['question']}",
                            reply_markup=test_second)