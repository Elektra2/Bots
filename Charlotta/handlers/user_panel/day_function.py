#Импорты
from aiogram import types
from config.bot_config import dp, bot
import aiocron
import datetime
from bd_handlers.materials.get_users import get_user_by_sd
from bd_handlers.materials.get_users import get_user_by_pd
from bd_handlers.user_profile.chage_user_role import change_role
from bd_handlers.subscription.change_update import change_update
from bd_handlers.subscription.change_final import change_final
from bd_handlers.subscription.change_final import post_count
from bd_handlers.subscription.change_id import change_id
from bd_handlers.subscription.change_post_date import change_post_date
from aiogram.utils.exceptions import BotBlocked

@aiocron.crontab('00 10 * * *')
async def days():
    sub_users = await get_user_by_sd(sd=datetime.date.today())
    for user_id in sub_users:
        try:
            await change_role(user_id=user_id['user_id'],score="basic")
            await change_update(user_id=user_id['user_id'])
            await bot.send_message(chat_id=user_id['user_id'],
                               text="У вас закончилась подписка Plus, вы можете заново подключить ее в настройках.")
        except BotBlocked:
            continue
    
    sub_end_users = await get_user_by_sd(sd=datetime.date.today()+datetime.timedelta(days=1))
    for user_id in sub_end_users:
        try:
            await change_update(user_id=user_id['user_id'])
            await bot.send_message(chat_id=user_id['user_id'],
                                text="Завтра заканчивается подписка Plus, вы можете продлить ее в настройках.")
        except BotBlocked:
            continue
    

@aiocron.crontab('00 10 * * *')
async def days_post():
    post_data =await get_user_by_pd(pd=datetime.date.today())
    for post in post_data:
        if post['test_comp'] == 1:
            n = await post_count(post_for=post['user_role'],post_lvl=post['score'])
            s = "post_id_"+post['user_role']
            id = post[s] + 1
            print(id,n-1)
            try:
                if id > n-1:
                    await change_final(user_id=post['user_id'])
                    await bot.send_message(chat_id=post['user_id'],
                                text=f"Вы закончили прохождения каруса для уровня {post['score']}. Чтобы перейти на новый уровень пройдите финальный тест в меню EduCourse.")
                else:
                    await change_id(user_id=post['user_id'],name=s)
                    if post['user_role'] == 'basic': date = datetime.date.today()+datetime.timedelta(days=7)
                    elif post['user_role'] == 'plus': date = datetime.date.today()+datetime.timedelta(days=4)
                    await change_post_date(user_id=post['user_id'],post_date=date)
                    await bot.send_message(chat_id=post['user_id'],
                                text="Вам доступны новые материалы🥳.")
            except BotBlocked:
                continue
        else:
            try:
                await change_post_date(user_id=post['user_id'],post_date=datetime.date.today()+datetime.timedelta(days=1))
                await bot.send_message(chat_id=post['user_id'],
                                text="Чтобы продолжить обучение пройдите тест.")
            except BotBlocked:
                continue