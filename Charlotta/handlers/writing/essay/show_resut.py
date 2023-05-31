from aiogram import types
import aiofiles
import aiohttp
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.writing.essay.show import FSM_show_writing
from bd_handlers.materials.get_user import get_user
from bd_handlers.writing.get_result import get_result
from aiogram.types import InputFile
import os


@dp.callback_query_handler(lambda c: c.data.startswith("result_id:"), state=FSM_show_writing.cur_list)
async def offer_process(callback_query:types.CallbackQuery, state:FSMContext):
    #SQL функция
    async with aiohttp.ClientSession() as session:
        s = list(callback_query.data.replace("result_id:", "").split('_'))
        file = f'./handlers/writing/essay/resultu{callback_query.from_user.id}.html'
        row = await get_result(post_lvl=s[0],post_lvl_id=int(s[1]),post_for=s[2], user_id=callback_query.from_user.id)
        back_to_list = types.InlineKeyboardMarkup().row(types.InlineKeyboardButton('Back to menu',callback_data='writing'))
        async with session.get(row['result']) as resp:
             f = await aiofiles.open(file, mode='wb')
             await f.write(await resp.read())
             await f.close()
        send = InputFile(file)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_document(chat_id=callback_query.from_user.id, 
                            caption=f"📑Score: {row['score']},\n📖Grade interpretation: {row['interpret']}",
                            document=send,
                            reply_markup=back_to_list)
        os.remove(file)
        