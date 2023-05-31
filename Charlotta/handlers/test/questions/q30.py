#Импорты
from handlers.test.question_dic import questions
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from bd_handlers.user_role.create_user import create_user
from handlers.test.start_test import FSM_test
from keyboards.test.second_test import second_test
from bd_handlers.user_profile.chage_user_score import change_score


#В этой функции записывается название поста
@dp.callback_query_handler(text='Q30_correct', state=FSM_test.Q30)
async def Q30(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q30'] = 4
        #Переходим к следующему состоянию
        await state.finish()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        s = sum(list(data.values())[2:])
        if int(s) in range(0,18): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/81R6j76w5Y',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='A1')
        elif int(s) in range(18,40): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/R04Zow0ZbF',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='A2')
        elif int(s)in range(40,60): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/0P23b21818',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='B1')
        elif int(s) in range(60,72): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/L3T63m2558',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='B2')
        elif int(s) == 72: 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/4j2QB590H7',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='C1')
        

@dp.callback_query_handler(text='Q30_incorrect', state=FSM_test.Q30)
async def Q30(callback_query: types.CallbackQuery, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['Q30'] = 0
        #Переходим к следующему состоянию
        await state.finish()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        #Отправляем сообщение
        s = sum(list(data.values())[2:])
        if int(s) in range(0,18): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/81R6j76w5Y',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='A1')
        elif int(s) in range(18,40): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/R04Zow0ZbF',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='A2')
        elif int(s)in range(40,60): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/0P23b21818',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='B1')
        elif int(s) in range(60,72): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/L3T63m2558',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='B2')
        elif int(s) == 72: 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/4j2QB590H7',
                               reply_markup=second_test)
            await create_user(user_id=int(data['user_id']), user_name=data['user_name'],score='C1')