import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values

#Файл с конфигами
config = dotenv_values(CONFIG_DIR / 'bot_config.env')


#Конфиги
USER = config['user']
PSWD = config['password']
DB = config['database']
HOST = config['host']


#Sql функция
async def create_test(test, post_for, post_id, post_lvl):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    await conn.execute('UPDATE posts SET test=$1'
                       'WHERE post_lvl_id=$2 AND post_lvl=$3 AND post_for=$4', 
                       test, post_id, post_lvl, post_for)
    await conn.close()
