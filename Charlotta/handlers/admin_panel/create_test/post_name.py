#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_test.show_post import FSM_create_test
import json
from bd_handlers.create_test.create_test import create_test

mas =[]

#В этой функции записывается изменение название поста
@dp.message_handler(state=FSM_create_test.post_name)
async def post_name(message: types.Message, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['post_name'] = int(message.text)
        #Переходим к следующему состоянию
        await FSM_create_test.next()
        #Отправляем сообщение
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Вставьте {1}/{data['post_name']} в формате словаря",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)

@dp.message_handler(state=FSM_create_test.post_test)
async def post_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        dct = json.loads(str(message.text))
        mas.append(dct)
        if len(mas) == data['post_name']:
            await FSM_create_test.next()
            await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
            await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"Введите кол-во процентов для успешного прохождения в формате 0.7",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)
        else:
            await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
            await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"Вставьте {len(mas)+1}/{data['post_name']} в формате словаря",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)
            

@dp.message_handler(state=FSM_create_test.questions)
async def post_name(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            array = [mas,[float(message.text)]]  
            await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
            await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"Вы успешно создали тест к записи {data['post_list']['post_lvl']}_{data['post_list']['post_lvl_id']} {data['post_list']['post_name']}",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)
            await create_test(test=str(array),post_id=data['post_list']['post_lvl_id'], post_lvl=data['post_list']['post_lvl'],post_for=data['post_list']['post_for'])