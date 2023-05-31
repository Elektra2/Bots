from aiogram import types
import aiofiles
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.writing.essay.show import FSM_show_writing
from bd_handlers.materials.get_post_name import get_post_name
from bd_handlers.writing.add_essay import add_essay
import requests
from jinja2 import Environment, FileSystemLoader
import os
import openai
import psycopg2
import threading
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
from keyboards.test.back_to_user_menu import user_panel_back_to_main_menu


#Файл с конфигами
config = dotenv_values(CONFIG_DIR / 'bot_config.env')


#Конфиги
user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])

openai.api_key = "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"

@dp.callback_query_handler(lambda c: c.data.startswith("offer_id:"), state=FSM_show_writing.cur_list)
async def offer_process(callback_query:types.CallbackQuery, state:FSMContext):
    #SQL функция
    s = list(callback_query.data.replace("offer_id:", "").split('_'))
    row = await get_post_name(post_lvl=s[0],post_id=int(s[1]),post_for=s[2])
    s.append(row['post_name'])
    back_to_list = types.InlineKeyboardMarkup().row(types.InlineKeyboardButton('Back to menu',callback_data='writing'))
    await state.update_data(post=s)
    await FSM_show_writing.next()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id, 
                           text=f"Напишите эссе для материала {row['post_name']}:",
                           reply_markup=back_to_list)
    

@dp.message_handler(state=FSM_show_writing.post)
async def writing_essay(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    threading.Thread(target=essay, args=(text,message.from_user.id,data)).start()
    await add_essay(user_id=message.from_user.id,post_lvl=data['post'][0],post_lvl_id=int(data['post'][1]),result="",score="",grade="None",interpret="",post_name=data['post'][3],post_for=data['post'][2])
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id-1)
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    back_to_list = types.InlineKeyboardMarkup().row(types.InlineKeyboardButton('Back',callback_data='writing_essay'))
    await bot.send_message(chat_id=message.from_user.id,
                           text="Ваше эссе принятно на проверку, вы сможете посмотреть результаты в разделе написанных эссе🥳",
                           reply_markup=user_panel_back_to_main_menu)
    
    

def essay(text,client_id,data1):
        env = Environment(loader=FileSystemLoader('./handlers/writing/template'))
        messages=[
        {"role": "user", "content":"Check out a neutral essay on British English, like the grammarly website. The examiner is familiar with the topic of the essay. In the answer, specify the correct version of the essay, indicating all the errors and rules that they violate, as well as the opinion of the examiner about initial essay and rating on a 100 scale. Form the response in json format with all errors, such as:{score:,modified_essay:,feedback:,mistakes:[{error:,correct:,rule:},...]}.Essay:"+f"{text}"}]
        response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages)
        otv={}
        otv['role'],otv['content'] = response['choices'][0]['message']['role'],response['choices'][0]['message']['content']
        data = eval(otv['content'])
        template = env.get_template("1.html")
        score = data['score']
        feedback = data['feedback']
        result = data['modified_essay']
        errors = []
        for error in data['mistakes']:
            rep = "<u>"+error['correct']+"</u>"
            result = result.replace(error['correct'],rep)
            errors.append({'mistake': error['error'],'disc': error['rule'],'correct':error['correct']})
        pdf_template = template.render(score=score, text=text.replace("\n","<br>"),result=result.replace("\n","<br>"),feedback=feedback, items=errors)
        file_path = f"./handlers/writing/essay/files/u{client_id}_{data1['post'][0]}_{data1['post'][1]}_{data1['post'][2]}.html"
        open(file_path,'w').write(pdf_template)
        username = "169779"
        password = "BS:b|4u_Za"
        container_name = "Materials"
        auth_token, storage_url = get_auth_token(username, password)
        result = upload_file_to_selectel(storage_url, auth_token, container_name, file_path, client_id,data1)
        os.remove(file_path)
        edit_essay(user_id=client_id,post_lvl=data1['post'][0],post_lvl_id=int(data1['post'][1]),result=result,score=str(score),interpret=feedback,post_for=data1['post'][2])

def edit_essay(user_id, post_lvl, post_lvl_id, result, score, interpret, post_for):
    conn = psycopg2.connect(user=user, password=password, database=database, host=host)
    conn.cursor().execute('''UPDATE writing SET result=%s, score=%s, interpret=%s WHERE user_id=%s AND post_lvl=%s AND post_lvl_id=%s AND post_for=%s''', (result, score, interpret,user_id, post_lvl, post_lvl_id,post_for))
    conn.commit()
    conn.close()

def get_auth_token(username, password):
        auth_url = "https://auth.selcdn.ru/"
        headers = {
            "X-Auth-User": username,
            "X-Auth-Key": password,
        }
        response = requests.post(auth_url, headers=headers)
        return response.headers["X-Storage-Token"], response.headers["X-Storage-Url"]

def upload_file_to_selectel(storage_url, auth_token, container_name, file_path, client_id,data):
        with open(file_path, "rb") as f:
            file_data = f.read()
        upload_url = f"{storage_url}/{container_name}/{file_path.split('/')[-1]}"
        headers = {
            "X-Auth-Token": auth_token,
        }
        requests.put(upload_url, headers=headers, data=file_data)
        return (f"https://585130.selcdn.ru/Materials/u{client_id}_{data['post'][0]}_{data['post'][1]}_{data['post'][2]}.html")
