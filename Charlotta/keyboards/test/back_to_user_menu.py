#Импорты
from aiogram import types


#Клавиатура "Админ Панель вернуться в главное меню"
user_panel_back_to_main_menu = types.InlineKeyboardMarkup()
#Кнопка admin_panel_btn_main_menu
usr_btn_mm = types.InlineKeyboardButton('Вернуться в главное меню',
                                       callback_data='main_user_menu')
#Добавляем кнопки в клавиатуру
user_panel_back_to_main_menu.row(usr_btn_mm)

user_panel_back_to_main_menu1 = types.InlineKeyboardMarkup()
#Кнопка admin_panel_btn_main_menu
usr_btn_mm = types.InlineKeyboardButton('Вернуться в главное меню',
                                       callback_data='main_user_menu1')
#Добавляем кнопки в клавиатуру
user_panel_back_to_main_menu1.row(usr_btn_mm)