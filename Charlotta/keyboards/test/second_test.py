#Импорты
from aiogram import types


#Клавиатура "Админ Панель вернуться в главное меню"
second_test = types.InlineKeyboardMarkup()
#Кнопка admin_panel_btn_main_menu
accept = types.InlineKeyboardButton('Принять результат',
                                       callback_data='main_user_menu1')
not_accept = types.InlineKeyboardButton('Попробовать еще раз',
                                       callback_data='start_second_test')
#Добавляем кнопки в клавиатуру
second_test.row(accept,not_accept)