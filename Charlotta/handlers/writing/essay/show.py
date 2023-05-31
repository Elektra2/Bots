from keyboards.writing.show_list import offers_kb
from keyboards.writing.show_result import result_kb
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.writing.writing import FSM_show_writing
from bd_handlers.materials.change_test import change_test
from bd_handlers.materials.get_post import get_posts
from bd_handlers.materials.get_user import get_user
from bd_handlers.writing.get_essay import get_essay
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.test.back_to_user_menu import user_panel_back_to_main_menu




@dp.callback_query_handler(text='writing_essay',state=FSM_show_writing.user)
async def post_list(callback_query: types.CallbackQuery, state=FSMContext ,n=5):
    users = await get_user(callback_query.from_user.id)
    post = []
    essay = await get_essay(callback_query.from_user.id)
    dictinary = {'basic':{'A1':[],'A2':[],'B1':[],'B2':[],'C1':[]},'plus':{'A1':[],'A2':[],'B1':[],'B2':[],'C1':[]}}
    if essay !=None or len(essay)==0:
        for i in essay:
            dictinary[i['post_for']][i['post_lvl']].append(i['post_lvl_id'])
    if users['post_comp_basic'] != None:
        s = list(users['post_comp_basic'].split(','))
        for i in s:
            list1 = await get_posts(i,"basic")
            for i in list1:
                if (i['writing'] == 1) and (i['post_lvl_id'] not in dictinary[i['post_for']][i['post_lvl']]):  post.insert(0,i)
    if users['post_comp_plus'] != None:
        s = list(users['post_comp_plus'].split(','))
        for i in s:
            list1 = await get_posts(i,"plus")
            for i in list1:
                if (i['writing'] == 1) and (i['post_lvl_id'] not in dictinary[i['post_for']][i['post_lvl']]):  post.insert(0,i)           
    new_post = await get_posts(users['score'],"basic")
    id = users['post_id_basic']
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id and new_post[i]['writing'] == 1 and (new_post[i]['post_lvl_id'] not in dictinary[new_post[i]['post_for']][new_post[i]['post_lvl']]):
            post.insert(0,new_post[i])
    new_post = await get_posts(users['score'],"plus")
    id = users['post_id_plus']
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id and new_post[i]['writing'] == 1 and (new_post[i]['post_lvl_id'] not in dictinary[new_post[i]['post_for']][new_post[i]['post_lvl']]):
            post.insert(0,new_post[i])
    comp = [True for i in range(len(post))]
    if users['see_post'] == 0: comp[0] = False
    posts = {'posts':post,'comp':comp}
    k = 0
    for i in range(len(posts['posts'])):
        if posts['comp'][i] and posts['posts'][i]['writing'] == 1: k+=1
    if k == 0:
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                                text="Извините, на данный момент вы написали все доступные эссе.✖️", 
                                reply_markup=user_panel_back_to_main_menu)
    else:
        await FSM_show_writing.next()
        await state.update_data(cur_list = n)   
        await bot.delete_message(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                                    text="Ваши материалы к которым вы можете написать эссе:", 
                                    reply_markup=offers_kb(posts, n))


@dp.callback_query_handler(lambda c: c.data.endswith("_offers"), state=FSM_show_writing.cur_list)#чтобы не писать отдельные хэндлеры для каждой функции, у каждой кнопке в каллбэк дате было дописано _offers, что мы здесь и проверяем. А также проверяем что state=cur_list(засетили его при первом вызове функции)
async def offers_process(callback_query:types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    users = await get_user(callback_query.from_user.id)
    match callback_query.data.replace("_offers", ""):
        case "forward":
            _cur_list = data.get("cur_list") + 5#нажата кнопка вперед, значит к желаемому индексу последнего товара прибавляем 10
        case "back":
            _cur_list = data.get("cur_list") - 5#аналогично, только теперь отнимаем
    
    post = []
    essay = await get_essay(callback_query.from_user.id)
    dictinary = {'basic':{'A1':[],'A2':[],'B1':[],'B2':[],'C1':[]},'plus':{'A1':[],'A2':[],'B1':[],'B2':[],'C1':[]}}
    if essay !=None or len(essay)==0:
        for i in essay:
            dictinary[i['post_for']][i['post_lvl']].append(i['post_lvl_id'])
    if users['post_comp_basic'] != None:
        s = list(users['post_comp_basic'].split(','))
        for i in s:
            list1 = await get_posts(i,"basic")
            for i in list1:
                if (i['writing'] == 1) and (i['post_lvl_id'] not in dictinary[i['post_for']][i['post_lvl']]):  post.insert(0,i)
    if users['post_comp_plus'] != None:
        s = list(users['post_comp_plus'].split(','))
        for i in s:
            list1 = await get_posts(i,"plus")
            for i in list1:
                if (i['writing'] == 1) and (i['post_lvl_id'] not in dictinary[i['post_for']][i['post_lvl']]):  post.insert(0,i)           
    new_post = await get_posts(users['score'],"basic")
    id = users['post_id_basic']
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id and new_post[i]['writing'] == 1 and (new_post[i]['post_lvl_id'] not in dictinary[new_post[i]['post_for']][new_post[i]['post_lvl']]):
            post.insert(0,new_post[i])
    new_post = await get_posts(users['score'],"plus")
    id = users['post_id_plus']
    for i in range(len(new_post)-1,-1,-1):
         if new_post[i]['post_lvl_id'] <= id and new_post[i]['writing'] == 1 and (new_post[i]['post_lvl_id'] not in dictinary[new_post[i]['post_for']][new_post[i]['post_lvl']]):
            post.insert(0,new_post[i])
    comp = [True for i in range(len(post))]
    if users['test_comp'] == 0: comp[0] = False
    posts = {'posts':post,'comp':comp}
    await state.update_data(cur_list = _cur_list)#вносим новый индекс
    await callback_query.message.edit_reply_markup(offers_kb(posts, _cur_list))

@dp.callback_query_handler(text='show_essay',state=FSM_show_writing.user)
async def post_list(callback_query: types.CallbackQuery, state=FSMContext ,n=5):
    essa = await get_essay(callback_query.from_user.id)
    essay = []
    for row in essa:
        print(row['result'])
        if row['result'] != "":
            essay.append(row)
    if essay == None or len(essay)==0:
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                                text="У вас нет написанных эссе✖️", 
                                reply_markup=user_panel_back_to_main_menu)
    else:
        await FSM_show_writing.next()
        await state.update_data(cur_list = n)   
        await bot.delete_message(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id)
        await bot.send_message(chat_id=callback_query.from_user.id,
                                    text="Ваши эссе 📔:", 
                                    reply_markup=result_kb(essay, n))


@dp.callback_query_handler(lambda c: c.data.endswith("_roffers"), state=FSM_show_writing.cur_list)#чтобы не писать отдельные хэндлеры для каждой функции, у каждой кнопке в каллбэк дате было дописано _offers, что мы здесь и проверяем. А также проверяем что state=cur_list(засетили его при первом вызове функции)
async def offers_process(callback_query:types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    essa = await get_essay(callback_query.from_user.id)
    essay = []
    for row in essa:
        if row['result'] != "":
            essay.append(row)
    match callback_query.data.replace("_offers", ""):
        case "forward":
            _cur_list = data.get("cur_list") + 5#нажата кнопка вперед, значит к желаемому индексу последнего товара прибавляем 10
        case "back":
            _cur_list = data.get("cur_list") - 5#аналогично, только теперь отнимаем
    
    await state.update_data(cur_list = _cur_list)#вносим новый индекс
    await callback_query.message.edit_reply_markup(result_kb(essay, _cur_list))