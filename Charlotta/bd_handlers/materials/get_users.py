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
async def get_user_by_pd(pd):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    rows = await conn.fetch('SELECT * FROM user_role WHERE post_date=$1',pd)
    await conn.close()
    if rows is None:
        return 'None'
    else:
        return rows

async def get_user_by_sd(sd):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    rows = await conn.fetch('SELECT * FROM user_role WHERE sub_date=$1',sd)
    await conn.close()
    if rows is None:
        return 'None'
    else:
        return rows