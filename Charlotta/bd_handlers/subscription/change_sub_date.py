#Импорты
import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values


#Файл с конфигами
config = dotenv_values(CONFIG_DIR / 'bot_config.env')


#Конфиги
user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])


#Sql функция
async def change_sub_date(user_id,sub_date):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute(f'UPDATE user_role SET sub_date=$1'
                       'WHERE user_id=$2',sub_date,user_id)
    await conn.close()
