#Импорты
from keyboards.post_list.show_list import offers_kb
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.show_post import FSM_change_post
from bd_handlers.post_list.show_posts import get_posts
from handlers.admin_panel.main_menu import admin_panel_main_menu_callback


#В этой функции записывается изменение описание поста
@dp.callback_query_handler(lambda c: c.data.endswith("_sp"),state=FSM_change_post.post_list)
async def post_list(callback_query: types.CallbackQuery, state: FSMContext, n=5):
    await  state.update_data(post_lvl = callback_query.data.replace("_sp",""))
    offers = await get_posts(callback_query.data.replace("_sp",""))
    await FSM_change_post.cur_list.set()
    await state.update_data(cur_list = n)#Для отслеживания конечной позиции
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text="Cписок записей:", 
                               reply_markup=offers_kb(offers, n))

@dp.callback_query_handler(lambda c: c.data.endswith("_offers"), state=FSM_change_post.cur_list)#чтобы не писать отдельные хэндлеры для каждой функции, у каждой кнопке в каллбэк дате было дописано _offers, что мы здесь и проверяем. А также проверяем что state=cur_list(засетили его при первом вызове функции)
async def offers_process(callback_query:types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    match callback_query.data.replace("_offers", ""):
        case "forward":
            _cur_list = data.get("cur_list") + 5#нажата кнопка вперед, значит к желаемому индексу последнего товара прибавляем 10
        case "back":
            _cur_list = data.get("cur_list") - 5#аналогично, только теперь отнимаем
    
    offers = await get_posts(data['post_lvl'])
    await state.update_data(cur_list = _cur_list)#вносим новый индекс
    await callback_query.message.edit_reply_markup(offers_kb(offers, _cur_list))#и для плавности работы не переотправляем сообщение, а просто изменяем уже отправленное сообщение
