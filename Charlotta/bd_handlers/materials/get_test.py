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
async def get_post_name(post_id, post_lvl, post_for):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    row = await conn.fetchrow('SELECT test FROM posts WHERE post_lvl_id=$1 AND post_lvl=$2 AND post_for=$3', post_id, post_lvl,post_for)
    await conn.close()
    if row is None:
        return 'None'
    else:
        return row['test']