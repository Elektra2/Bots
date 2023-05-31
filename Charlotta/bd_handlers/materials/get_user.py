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
async def get_user(user_id):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    rows = await conn.fetchrow('SELECT * FROM user_role WHERE user_id=$1',user_id)
    await conn.close()
    if rows is None:
        return 'None'
    else:
        return rows
