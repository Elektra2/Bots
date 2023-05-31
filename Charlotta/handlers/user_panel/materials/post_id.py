#Импорты
from keyboards.materials.back import back_to_list
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.user_panel.materials.post_list import FSM_show_post
from bd_handlers.materials.get_post_name import get_post_name
from bd_handlers.materials.get_user import get_user
from bd_handlers.materials.change_state import change_state


#В этой функции записывается изменение название поста
@dp.callback_query_handler(lambda c: c.data.startswith("offer_id:"), state=FSM_show_post.cur_list)
async def offer_process(callback_query:types.CallbackQuery, state:FSMContext):
    #SQL функция
    users = await get_user(callback_query.from_user.id)
    s = list(callback_query.data.replace("offer_id:", "").split('_'))
    post_id = 'post_id_'+users['user_role']
    if(users['score']==s[0] and users[post_id]==int(s[1]) and users['user_role'] == s[2]): 
        await change_state(user_id=callback_query.from_user.id)
    row = await get_post_name(post_lvl=s[0],post_id=int(s[1]),post_for=s[2])
    await FSM_show_post.previous()
    await state.update_data(post_name = 1)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    m1 = await bot.send_photo(chat_id=callback_query.from_user.id,
                                photo="https://www.flickr.com/photos/197797038@N06/shares/ER4U9F00Uz",
                                caption=row['post_text'])
    m2 = await bot.send_voice(chat_id=callback_query.from_user.id,
                              voice=row['voice'])
    m3 = await bot.send_document(chat_id=callback_query.from_user.id,
                                 document=row['post_photo'],
                                 reply_markup=back_to_list)
    messages = [m1.message_id,m2.message_id,m3.message_id]
    await state.update_data(post = messages)
    