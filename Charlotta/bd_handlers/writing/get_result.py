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
async def get_result(user_id, post_for, post_lvl_id, post_lvl):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    rows = await conn.fetchrow('SELECT * FROM writing WHERE user_id=$1 AND post_for=$2 AND post_lvl_id=$3 AND post_lvl=$4',user_id, post_for, post_lvl_id, post_lvl)
    await conn.close()
    if rows is None:
        return 'None'
    else:
        return rows