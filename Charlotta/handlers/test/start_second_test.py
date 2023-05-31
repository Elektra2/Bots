#Импорты
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.test.back_to_user_menu import user_panel_back_to_main_menu1
from bd_handlers.user_profile.chage_user_score import change_score



class FSM_test(StatesGroup):
    question =State()
    list = State()
    score = State()



#То что происходит после нажатия кнокпи "Создать пост"
@dp.callback_query_handler(text='start_second_test')
async def Q1(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_test.question.set()

    await state.update_data(question = 0)
    await state.update_data(score = 0)
    await state.update_data(list = [{"question": "Can I park my car here?", "options": ["a) Sorry, I did that", "b) Only for an hour", "c) It's the same place", "d) I am not sure / Я не уверен(а)"], "answer": 1, "number": "1", "points": 1, "photo": "https://www.flickr.com/photos/197797038@N06/shares/H2Z8cdM678"},
 {"question": "What colour will you paint the parent's bedroom?", "options": ["a) I hope it was right.", "b) We can't decide.", "c) It wasn't hard.", "d) I am not sure / Я не уверен(а)"], "answer": 1, "number": "2", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/8WUz34x191"},
 {"question": "I can't understand this task.", "options": ["a) Would you like some help?", "b) Don't you know?", "c) I suppose you can.", "d) I am not sure / Я не уверен(а)"], "answer": 0, "number": "3", "points": 2, "photo": "https://www.flickr.com/photos/197797038@N06/shares/g917nH1ST7"},
 {"question": "I'd like two tickets for the Grand Show tomorrow.", "options": ["a) What did you pay?", "b) Evening and afternoon.", "c) I'll just check for you.", "d) I am not sure / Я не уверен(а)"], "answer": 2, "number": "4", "points": 2, "photo": "https://www.flickr.com/photos/197797038@N06/shares/9C14R50nd8"},
 {"question": "I like to _______ TV in the evening.", "options": ["a) watch", "b) watched", "c) watching", "d) watches", "e) I am not sure / Я не уверен(а)"], "answer": 0, "number": "5", "points": 1, "photo": "https://www.flickr.com/photos/197797038@N06/shares/PZ04Z09J98"},
 {"question": "His eyes were ________ bad that he couldn't read his homework on the blackboard.", "options": ["a) such", "b) very", "c) too", "d) so", "e) I am not sure / Я не уверен(а)"], "answer": 3, "number": "6", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/g9BL9M4Kv6"},
 {"question": "The organization needs to decide _______ and for all what its position is on this point.", "options": ["a) finally", "b) once", "c) here", "d) I am not sure / Я не уверен(а)"], "answer": 1, "number": "7", "points": 5, "photo": "https://www.flickr.com/photos/197797038@N06/shares/k5X811mgKz"},
 {"question": "Don't put your coffee on the ________ of the table – someone will knock it off.", "options": ["a) outside", "b) boundary", "c) border", "d) edge", "e) I am not sure / Я не уверен(а)"], "answer": 3, "number": "8", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/3gM7S0xrDY"},
 {"question": "Sorryyyyy - I didn't ______ to disturb you.", "options": ["a) suppose", "b) think", "c) hope", "d) mean", "e) I am not sure / Я не уверен(а)"], "answer": 3, "number": "9", "points": 4, "photo": "https://www.flickr.com/photos/197797038@N06/shares/W18k715r5k"},
 {"question": "Ariana Grande ended the concert _______ her song \"7 rings\".", "options": ["a) by", "b) with", "c) on", "d) as", "e) I am not sure / Я не уверен(а)"], "answer": 1, "number": "10", "points": 1, "photo": "https://www.flickr.com/photos/197797038@N06/shares/4RYkj76T9V"},
 {"question": "Would you mind _______ these plates a wipe before putting them in the locker?", "options": ["a) giving", "b) doing", "c) getting", "d) taking", "e) I am not sure / Я не уверен(а)"], "answer": 0, "number": "11", "points": 4, "photo": "https://www.flickr.com/photos/197797038@N06/shares/EzqzL4WhN3"},
 {"question": "He was looking forward _______ at the new cafe, but it was closed.", "options": ["a) to eat", "b) to eating", "c) to have eaten", "d) eating", "e) I am not sure / Я не уверен(а)"], "answer": 1, "number": "12", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/N317z29X93"},
 {"question": "_______ tired Irina is when she gets home from work, she always makes time to make a dinner for her dad.", "options": ["a) Whatever", "b) No matter how", "c) However much", "d) Although", "e) I am not sure / Я не уверен(а)"], "answer": 1, "number": "13", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/0BLamB903T"},
 {"question": "It was only twelve days ago ________ he started his new job at the university", "options": ["a) then", "b) that", "c) since", "d) after", "e) I am not sure / Я не уверен(а)"], "answer": 1, "number": "14", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/5Pbc529127"},
 {"question": "The sports shop didn't have the trainers I wanted, but they've _______ a pair specially for me.", "options": ["a) ordered", "b) booked", "c) commanded", "d) asked", "e) I am not sure / Я не уверен(а)"], "answer": 0, "number": "15", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/0CX497ezmd"},
 {"question": "Have you got time to discuss your business now with Donald Trump or are you ______ to leave?", "options": ["a) thinking", "b) round", "c) about", "d) planned", "e) I am not sure / Я не уверен(а)"], "answer": 2, "number": "16", "points": 5, "photo": "https://www.flickr.com/photos/197797038@N06/shares/29rbFBQmSk"},
 {"question": "Faiz came to live here _______ a month ago.", "options": ["a) quite", "b) already", "c) almost", "d) beyond", "e) I am not sure / Я не уверен(а)"], "answer": 2, "number": "17", "points": 2, "photo": "https://www.flickr.com/photos/197797038@N06/shares/YaYq012878"},
 {"question": "Once the rocket is in the space, you can ______ your seat belts if you wish.", "options": ["a) untie", "b) brake", "c) unlock", "d) unfasten", "e) I am not sure / Я не уверен(а)"], "answer": 3, "number": "18", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/Ei1mr9J8e8"},
 {"question": "I left my favorite job because I had no ______ to travel around the world.", "options": ["a) place", "b) opportunity", "c) possibility", "d) position", "e) I am not sure / Я не уверен(а)"], "answer": 1, "number": "19", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/oiL451Ti97"},
 {"question": "It wasn't a bad crash and ______ damage was done to my Mercedes.", "options": ["a) little", "b) small", "c) light", "d) mere", "e) I am not sure / Я не уверен(а)"], "answer": 0, "number": "20", "points": 4, "photo": "https://www.flickr.com/photos/197797038@N06/shares/iCTk577s0q"},
 {"question": "I'd rather you ______ to him why we can't go.", "options": ["a) would explain", "b) explained", "c) will explain", "d) to explain", "e) I am not sure / Я не уверен(а)"], "answer": 1, "number": "21", "points": 5, "photo": "https://www.flickr.com/photos/197797038@N06/shares/0S487000J9"},
 {"question": "Before making a decision, the boss considered all _____ of the argument.", "options": ["a) features", "b) sides", "c) perspectives", "d) shades", "I am not sure / Я не уверен(а)"], "answer": 1, "number": "22", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/sBdR3U8UJ9"},
 {"question": "This new PC is recommended as being ______ reliable.", "options": ["a) greatly", "b) strongly", "c) readily", "d) highly", "e) I am not sure / Я не уверен(а)"], "answer": 3, "number": "23", "points": 3, "photo": "https://www.flickr.com/photos/197797038@N06/shares/837L66Ymb8"},
 {"question": "When I realised I had dropped my Iphone, I decided to ______ my steps.", "options": ["a) retrace", "b) regress", "c) resume", "d) return", "e) I am not sure / Я не уверен(а)"], "answer": 0, "number": "24", "points": 5, "photo": "https://www.flickr.com/photos/197797038@N06/shares/EMovp1uk1r"},
 {"question": "Gleb's house is somewhere in the ______ of the train station.", "options": ["a) region", "b) district", "c) quarter", "d) vicinity", "e) I am not sure / Я не уверен(а)"], "answer": 3, "number": "25", "points": 4, "photo": "https://www.flickr.com/photos/197797038@N06/shares/J47FY0M0J6"}])
    #Удаляем предидущее сообщение
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


@dp.callback_query_handler(lambda c: c.data.startswith("options_"), state=FSM_test.question)
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
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=data['list'][next_q]['photo'], caption=f"Вопрос {next_q+1}/{len(data['list']):}:\n{data['list'][next_q]['question']}",
                           reply_markup=test_options)
    else:
        s = score
        await state.finish()
        await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
        if int(s) in range(0,8): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/81R6j76w5Y',
                               reply_markup=user_panel_back_to_main_menu1)
            await change_score(score= 'A1', user_id=callback_query.from_user.id)
        elif int(s) in range(8,25): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/R04Zow0ZbF',
                               reply_markup=user_panel_back_to_main_menu1)
            await change_score(score= 'A2', user_id=callback_query.from_user.id)
        elif int(s)in range(25,46): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/0P23b21818',
                               reply_markup=user_panel_back_to_main_menu1)
            await change_score(score= 'B1', user_id=callback_query.from_user.id)
        elif int(s) in range(46,71): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/L3T63m2558',
                               reply_markup=user_panel_back_to_main_menu1)
            await change_score(score= 'B2', user_id=callback_query.from_user.id)
        elif int(s) in range(71,79): 
            await bot.send_photo(chat_id=callback_query.from_user.id,
                               photo ='https://www.flickr.com/photos/197797038@N06/shares/4j2QB590H7',
                               reply_markup=user_panel_back_to_main_menu1)
            await change_score(score= 'C1', user_id=callback_query.from_user.id)