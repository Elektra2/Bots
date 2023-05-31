#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.show_post import FSM_change_post
from bd_handlers.change_post.get_post_name import get_post_name


#В этой функции записывается изменение название поста
@dp.callback_query_handler(lambda c: c.data.startswith("offer_id:"), state=FSM_change_post.cur_list)
async def offer_process(callback_query:types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        #SQL функция
        print(callback_query.data.replace("offer_id:", ""))
        s = list(callback_query.data.replace("offer_id:", "").split('_'))
        row = await get_post_name(int(s[0]),data['post_lvl'],s[1])
        #Переходим к следующему состоянию
        data['post_list'] = dict(row)
        await FSM_change_post.next()
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        #Отправляем сообщение
        await bot.send_message(chat_id=callback_query.from_user.id,
                                text=f"Имя записи: {row['post_name']}\n"
                                f"Введите новое имя записи:\n",
                                reply_markup=admin_panel_keyboard_back_to_main_menu)