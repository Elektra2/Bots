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
async def edit_essay(user_id, post_lvl, post_lvl_id, result, score, interpret, post_for):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''UPDATE writing SET result=$1, score=$2, interpret=$3 WHERE user_id=$4, post_lvl=$5, post_lvl_id=$6, post_for=$7''', result, score, interpret,user_id, post_lvl, post_lvl_id,post_for)
    await conn.close()