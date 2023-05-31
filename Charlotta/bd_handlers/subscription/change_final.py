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
async def change_final(user_id):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('UPDATE user_role SET final_test=$1'
                       'WHERE user_id=$2',1,user_id)
    await conn.close()

async def post_count(post_lvl,post_for):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    row = await conn.fetch('SELECT post_name FROM posts WHERE post_lvl = $1 AND post_for = $2', post_lvl, post_for)
    return len(row)