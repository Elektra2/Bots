import asyncpg
import aiohttp
import json
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
from googletrans import Translator

#Файл с конфигами
config = dotenv_values(CONFIG_DIR / 'bot_config.env')


#Конфиги
user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])


#Sql функция
async def create_post(post_name, post_text, post_photo, post_lvl, user_name, create_data, create_time, post_for, writing):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    row = await conn.fetch('SELECT post_name FROM posts WHERE post_lvl = $1 AND post_for = $2', post_lvl, post_for)
    if row is None: size=0
    else: size = len(row)
    file = await ozvuch(post_text)
    await conn.execute('''INSERT INTO posts(post_name, post_text, post_photo, post_lvl, user_name, create_data, create_time, post_lvl_id, post_for, voice, writing)
                       VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)''',
                       post_name, post_text, post_photo, post_lvl, user_name, create_data, create_time, size, post_for, file, writing)
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
    v