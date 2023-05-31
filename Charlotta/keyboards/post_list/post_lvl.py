#Импорты
from aiogram import types


#Клавиатура "Админ Панель выбрать роль"
show_post_lvl = types.InlineKeyboardMarkup()
#Кнопка Администратор
sp_a1 = types.InlineKeyboardButton('A1',
                                       callback_data='A1_sp')
#Кнопка Контент Менеджер
sp_a2 = types.InlineKeyboardButton('A2',
                                       callback_data='A2_sp')
sp_b1 = types.InlineKeyboardButton('B1',
                                       callback_data='B1_sp')
sp_b2 = types.InlineKeyboardButton('B2',
                                       callback_data='B2_sp')
sp_c1 = types.InlineKeyboardButton('C1',
                                       callback_data='C1_sp')
ap_btn_mm = types.InlineKeyboardButton('Вернуться в главное меню',
                                       callback_data='main_menu')

show_post_lvl.row(sp_a1,sp_a2)
show_post_lvl.row(sp_b1,sp_b2)
show_post_lvl.row(sp_c1)
show_post_lvl.row(ap_btn_mm)