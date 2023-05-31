#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.test.back_to_user_menu import user_panel_back_to_main_menu
from bd_handlers.user_profile.profile import bd_profile
from bd_handlers.user_profile.chage_user_role import change_role
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import InputMediaPhoto
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters.state import State, StatesGroup
import datetime
from bd_handlers.subscription.get_users import get_user_sub
from bd_handlers.subscription.change_sub_date import change_sub_date

class FSM_back(StatesGroup):
    back = State()


#То что происходит после нажатия кнокпи "Выйти в главное меню"
@dp.callback_query_handler(text='subscribe', state='*')
async def subscribe(callback_query: types.CallbackQuery, state: FSMContext):
    user = await bd_profile(callback_query.from_user.id)
    await FSM_back.back.set()
    back = types.InlineKeyboardMarkup()
    if user['update'] == 1: back.row(types.InlineKeyboardButton('Купить💳',callback_data='buy'))
    back.row(types.InlineKeyboardButton('Назад',callback_data='show_profile1'))
    pictures = [
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/66THpL3X0M", caption="Basic"),
            InputMediaPhoto(media="https://www.flickr.com/photos/197797038@N06/shares/0621718w37", caption="Plus")]
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    await bot.send_media_group(chat_id=callback_query.from_user.id, 
                                media=pictures)
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Я рада предложить вам два доступных уровня подписки: Basic и Plus. Basic предоставляется абсолютно бесплатно, в то время как Plus обходится в 299 рублей ежемесячно. Пожалуйста, ознакомьтесь с деталями каждой подписки на картинках выше. Чтобы приобрести подписку Plus, нажмите кнопку \"Купить💳\".",
                               reply_markup=back)

@dp.callback_query_handler(text='buy', state=FSM_back.back)
async def buy(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id-2)
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id-1)
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    back = types.InlineKeyboardMarkup()
    back.row(types.InlineKeyboardButton('Оплатить 299Руб',pay=True))
    back.row(types.InlineKeyboardButton('Назад',callback_data='show_profile2'))
    await bot.send_invoice(chat_id=callback_query.from_user.id, title="Оформление подписки Plus", description="Подписка Plus", payload="sub", provider_token="390540012:LIVE:33233", need_email= True, send_email_to_provider= True, provider_data={"receipt": {"items":[{"description":"Подписка Plus","quantity":"1.00","amount":{"value":"299.00","currency":"RUB"}, "vat_code":1}]}}, currency="RUB", start_parameter="test", prices=[{'label':'Руб','amount':29900}],reply_markup=back)

@dp.pre_checkout_query_handler(state=FSM_back.back)
async def pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT,state=FSM_back.back)
async def process_pay(message: types.Message,state: FSMContext):
    if message.successful_payment.invoice_payload == "sub":
        await change_role(user_id=message.from_user.id,score="plus")
        now = datetime.date.today()
        sub = get_user_sub(user_id=message.from_user.id)
        if now>sub:
            await change_sub_date(user_id=message.from_user.id,sub_date=now+datetime.timedelta(days=30))
        else:
            await change_sub_date(user_id=message.from_user.id,sub_date=sub+datetime.timedelta(days=30))
        await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
        await bot.send_message(chat_id=message.from_user.id,
                               text="Подписка успешна оплачена✅",
                               reply_markup=user_panel_back_to_main_menu)