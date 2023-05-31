#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.user_panel.user_main_menu import user_main_menu
from aiogram.dispatcher import FSMContext
from bd_handlers.user_role.get_user_name import get_user_name
from aiogram.dispatcher.filters.state import State, StatesGroup
from bd_handlers.subscription.change_sub_date import change_sub_date
import datetime


#То что происходит после нажатия кнокпи "Выйти в главное меню"
@dp.callback_query_handler(text='main_user_menu',state='*')
async def admin_panel_main_menu_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    #Удаляем предидущее сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    user_id = int(callback_query.from_user.id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Привет, {await get_user_name(user_id=user_id)}",
                               reply_markup=user_main_menu)

@dp.callback_query_handler(text='main_user_menu1',state='*')
async def admin_panel_main_menu_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    #Удаляем предидущее сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    old_user=[6010818245, 1944239175, 2043387825, 1098811113, 1167952120, 5202820580, 2086503521, 998021237, 446648849, 488478275, 577863650, 637221619, 778399798, 1010557294, 424529873, 1158108962, 1254279146, 5127305143, 5119701116, 5811156804, 5427566680, 1023682855, 287805367, 5108679467, 859193249, 5417975863, 646053441, 492784510, 257804183, 233611100, 1196581714, 1647025321, 6134364627, 1485131365, 1904126715, 6015120470, 6234775686, 6181412943, 5778633603, 5615747078, 5166235594, 5141272144, 5107742630, 2020811599, 1595186107, 1337960628, 1255104607, 1228427724, 841873995, 835341619, 828455611, 825961269, 759043515, 740149214, 711520605, 644095371, 581204085, 563374445, 744599193, 578797856]
    user_id = callback_query.from_user.id
    if user_id in old_user:
        await change_sub_date(user_id=callback_query.from_user.id, sub_date=datetime.date.today()+datetime.timedelta(days=30))
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text="С возвращением! 🤗 Чтобы отблагодарить вас за активное участие в бета-тестировании, вы получаете 30 дней бесплатного доступа к подписке уровня Plus! Наслаждайтесь расширенными функциями и эксклюзивными возможностями! 😍")
    else:
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text="Как новому пользователю, вам доступно 5 дней бесплатного доступа к уровню подписки Plus! Наслаждайтесь расширенными функциями и эксклюзивными возможностями без ограничений!😍")
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Привет, {await get_user_name(user_id=user_id)}",
                               reply_markup=user_main_menu)