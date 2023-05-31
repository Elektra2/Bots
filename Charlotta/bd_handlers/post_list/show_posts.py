import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
import asyncio

#Файл с конфигами
config = dotenv_values(CONFIG_DIR / 'bot_config.env')


#Конфиги
USER = config['user']
PSWD = config['password']
DB = config['database']
HOST = config['host']


async def get_posts(post_lvl):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    rows = await conn.fetch('SELECT * FROM posts WHERE post_lvl=$1 ORDER BY create_data DESC, create_time DESC',post_lvl)
    await conn.close()
    if rows is None:
        return 'None'
    else:
        return rows