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
async def get_posts(score,user_role):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    rows = await conn.fetch('SELECT * FROM posts WHERE post_lvl=$1 AND post_for=$2 ORDER BY post_lvl_id DESC',score,user_role)
    await conn.close()
    if rows is None:
        return 'None'
    else:
        return rows
