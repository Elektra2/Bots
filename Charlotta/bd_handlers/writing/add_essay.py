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
async def add_essay(user_id, post_lvl, post_lvl_id, result, score, grade, interpret, post_name,post_for):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''INSERT INTO writing(user_id, post_lvl, post_lvl_id, result, score, grade, interpret, post_name,post_for) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9)''',user_id, post_lvl, post_lvl_id, result, score, grade, interpret, post_name,post_for)
    await conn.close()