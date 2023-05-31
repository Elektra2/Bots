import asyncpg
import aiohttp
import json
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
from googletrans import Translator
#Файл с конфигами
config = dotenv_values(CONFIG_DIR / 'bot_config.env')


#Конфиги
USER = config['user']
PSWD = config['password']
DB = config['database']
HOST = config['host']


#Sql функция
async def change_post(post_name, post_text, post_for, post_photo, change_user_name, change_date, change_time, post_id, post_lvl, writing):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    file = await ozvuch(post_text)
    await conn.execute('UPDATE posts SET post_name=$1, post_text=$2, post_photo=$3, change_user_name=$4, change_date=$5, change_time=$6, voice=$10, writing=$11'
                       'WHERE post_lvl_id=$7 AND post_lvl=$8 AND post_for=$9', 
                       post_name, post_text, post_photo, change_user_name, change_date, change_time, post_id, post_lvl, post_for,file,writing)
    await conn.close()

async def ozvuch(txt):
    async with aiohttp.ClientSession() as session:
        translator = Translator()
        txt = translator.translate(text=txt, dest='en').text
        data = {'token':'b99a08c606bc54d6bddd0a0b44071385',
        'email':'glebchiksolovev@gmail.com',
        'voice':'Ashley',
        'text': txt, 
        'format':'mp3',
        'speed':1.1, 
        'emotion':'good',}
        js =  json.loads(await (await session.post('https://zvukogram.com/index.php?r=api/text', data=data)).text())
        voice = str(js['file']).replace('\\','')
        return voice 