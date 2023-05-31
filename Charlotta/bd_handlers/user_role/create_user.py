#Импорты
import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
import datetime

#Файл с конфигами
config = dotenv_values(CONFIG_DIR / 'bot_config.env')


#Конфиги
user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])


#Sql функция
async def create_user(user_id, user_name, score):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''INSERT INTO user_role(user_id, user_role, user_name, score, post_id_basic, see_post, test_comp, post_date, update, final_test, test_count, post_id_plus, sub_date) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)''', user_id, 'plus', user_name, score, 0, 0, 0,datetime.date.today()+datetime.timedelta(days=4),0,0,3,0,datetime.date.today()+datetime.timedelta(days=5))
    await conn.close()