#Импорты
from keyboards.materials.show_list import offers_kb
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from bd_handlers.materials.change_test import change_test
from bd_handlers.materials.get_post import get_posts
from bd_handlers.materials.get_user import get_user
from bd_handlers.materials.get_test import get_post_name
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.test.back_to_user_menu import user_panel_back_to_main_menu
import random


class FSM_show_post(StatesGroup):
    user = State()
    cur_list = State()
    post_name = State()
    post = State()
    tst = State()
    question =State()
    list = State()
    score = State()

@dp.callback_query_handler(text='show_material')
async def materials(callback_query: types.CallbackQuery, state=FSMContext):
    users = await get_user(callback_query.from_user.id)
    await FSM_show_post.user.set()
    await state.update_data(post_name = 0)
    mat_btn = types.InlineKeyboardMarkup()
    if users['see_post'] == 1 and users['test_comp'] == 0:
        mat_btn.row(types.InlineKeyboardButton('See materials🔎',callback_data='materials'),types.InlineKeyboardButton('Test🧑‍💻',callback_data='test'))
    else: mat_btn.row(types.InlineKeyboardButton('See materials🔎',callback_data='materials'))
    mat_btn.row(types.InlineKeyboardButton('Вернуться в главное меню',callback_data='main_user_menu'))
    await bot.delete_message(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                                text="Здесь будут отоброжаться все ваши материалы и доступные тесты", 
                                reply_markup=mat_btn)



#В этой функции записывается изменение описание поста
@dp.callback_query_handler(text='materials',state=FSM_show_post.user)
async def post_list(callback_query: types.CallbackQuery, state=FSMContext ,n=5):
    users = await get_user(callback_query.from_user.id)
    data = await state.get_data()
    post = []
    if users['post_comp_basic'] != None:
        s = list(users['post_comp_basic'].split(','))
        for i in s:
            list1 = await get_posts(i,"basic")
            post = [*list1,*post]
    if users['post_comp_plus'] != None:
        s = list(users['post_comp_plus'].split(','))
        for i in s:
            list1 = await get_posts(i,"plus")
            post = [*list1,*post]
    new_post = await get_posts(users['score'],"basic")
    id = users["post_id_basic"]
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id:
            post.insert(0,new_post[i])
    new_post = await get_posts(users['score'],"plus")
    id = users["post_id_plus"]
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id:
            post.insert(0,new_post[i])
    comp = [True for i in range(len(post))]
    if len(comp) == 0:
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                                text="Извените, у меня для вас пока нет заданий.", 
                                reply_markup=user_panel_back_to_main_menu)
    else:
        if users['test_comp'] == 0: comp[0] = False
        posts = {'posts':post,'comp':comp}
        await FSM_show_post.next()
        await state.update_data(cur_list = n)
        if data['post_name'] == 1:
            mes = data['post']
            for i in mes:
                await bot.delete_message(chat_id=callback_query.from_user.id,
                                message_id=i)
            await state.update_data(post_name = 0)
            await state.update_data(post = [])
            await bot.send_message(chat_id=callback_query.from_user.id,
                                    text="Ваши записи:", 
                                    reply_markup=offers_kb(posts, n))
        else:   
            await bot.delete_message(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id)
            await bot.send_message(chat_id=callback_query.from_user.id,
                                    text="Ваши записи:", 
                                    reply_markup=offers_kb(posts, n))


@dp.callback_query_handler(lambda c: c.data.endswith("_offers"), state=FSM_show_post.cur_list)#чтобы не писать отдельные хэндлеры для каждой функции, у каждой кнопке в каллбэк дате было дописано _offers, что мы здесь и проверяем. А также проверяем что state=cur_list(засетили его при первом вызове функции)
async def offers_process(callback_query:types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    users = await get_user(callback_query.from_user.id)
    match callback_query.data.replace("_offers", ""):
        case "forward":
            _cur_list = data.get("cur_list") + 5#нажата кнопка вперед, значит к желаемому индексу последнего товара прибавляем 10
        case "back":
            _cur_list = data.get("cur_list") - 5#аналогично, только теперь отнимаем
    
    post = []
    if users['post_comp_basic'] != None:
        s = list(users['post_comp_basic'].split(','))
        for i in s:
            list1 = await get_posts(i,"basic")
            post = [*list1,*post]
    if users['post_comp_plus'] != None:
        s = list(users['post_comp_plus'].split(','))
        for i in s:
            list1 = await get_posts(i,"plus")
            post = [*list1,*post]
    new_post = await get_posts(users['score'],"basic")
    id = users["post_id_basic"]
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id:
            post.insert(0,new_post[i])
    new_post = await get_posts(users['score'],"plus")
    id = users["post_id_plus"]
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id:
            post.insert(0,new_post[i])
    comp = [True for i in range(len(post))]
    if users['test_comp'] == 0: comp[0] = False
    posts = {'posts':post,'comp':comp}
    await state.update_data(cur_list = _cur_list)#вносим новый индекс
    await callback_query.message.edit_reply_markup(offers_kb(posts, _cur_list))#и для плавности работы не переотправляем сообщение, а просто изменяем уже отправленное сообщение

@dp.callback_query_handler(text='test',state=FSM_show_post.user)
async def post_list(callback_query: types.CallbackQuery, state=FSMContext ,n=5):
    users = await get_user(callback_query.from_user.id)
    await FSM_show_post.question.set()
    post_id = 'post_id_'+users['user_role']
    test = eval(await get_post_name(post_for=users['user_role'],post_lvl=users['score'],post_id=users[post_id]))
    await state.update_data(question = 0)
    await state.update_data(score = 0)
    await state.update_data(list = random.sample(test[0],10))
    await state.update_data(tst = test[1][0])
    data = await state.get_data()
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    test_options = types.InlineKeyboardMarkup()
    otv = data['list'][data['question']]['options']
    for i in range(len(otv)):
        if i == data['list'][data['question']]['answer']:
            test_options.row( types.InlineKeyboardButton(otv[i], callback_data='options_correct'))
        else:
            test_options.row( types.InlineKeyboardButton(otv[i], callback_data='options_incorrect'))
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=data['list'][data['question']]['photo'], caption=f"Вопрос 1/{len(data['list'])}:\n{data['list'][data['question']]['question']}",
                           reply_markup=test_options)


@dp.callback_query_handler(lambda c: c.data.startswith("options_"), state=FSM_show_post.question)
async def offer_process(callback_query:types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    otv = callback_query.data.replace("options_", "")
    score = data['score']+data['list'][data['question']]['points']
    if otv == 'correct': await state.update_data(score = score)
    next_q = data['question']+1
    await state.update_data(question = next_q)
    if next_q != len(data['list']):
        test_options = types.InlineKeyboardMarkup()
        otv = data['list'][next_q]['options']
        for i in range(len(otv)):
            if i == data['list'][next_q]['answer']:
                test_options.row( types.InlineKeyboardButton(otv[i], callback_data='options_correct'))
            else:
                test_options.row( types.InlineKeyboardButton(otv[i], callback_data='options_incorrect'))
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=data['list'][next_q]['photo'], caption=f"Вопрос {next_q+1}/{len(data['list'])}:\n{data['list'][next_q]['question']}",
                           reply_markup=test_options)
    else:
        s = score
        await state.finish()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        if s < data['tst']*10:
            await bot.send_message(chat_id=callback_query.from_user.id,
                                text=f"Попробуйте пройти тест еще раз и набрать минимум {data['tst']*100}% от общего числа баллов, чтобы завершить урок. На данный момент у вас - {s/10*100}%.", 
                                reply_markup=user_panel_back_to_main_menu)
        else:
            await change_test(callback_query.from_user.id)
            await bot.send_message(chat_id=callback_query.from_user.id,
                                text=f"Well done! Вы прошли урок успешно!",
                                reply_markup=user_panel_back_to_main_menu)