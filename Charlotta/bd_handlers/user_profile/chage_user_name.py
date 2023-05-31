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
async def change_name(score, user_id):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    await conn.execute('UPDATE user_role SET user_name=$1'
                       'WHERE user_id=$2', 
                       score,user_id)
    await conn.close()