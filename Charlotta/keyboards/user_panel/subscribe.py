#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
settings_menu = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
usr_btn_sub =types.InlineKeyboardButton('plus',
                                       callback_data='sub_plus')
usr_btn_set =types.InlineKeyboardButton('Пройти тест на уровень повторно',
                                       callback_data='sub_basic')
#Кнопка cm_keyboard_btn_delete_post
usr_btn_mm = types.InlineKeyboardButton('Назад',
                                       callback_data='show_profile')
#Кнопка cm_keyboard_btn_change_post


#Клавиатура cm_keyboard_main_menu
settings_menu.row(usr_btn_set,usr_btn_sub)
settings_menu.row(usr_btn_mm)