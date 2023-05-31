#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
profile_menu = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
usr_btn_sub =types.InlineKeyboardButton('Подписки',
                                       callback_data='subscribe')
usr_btn_set =types.InlineKeyboardButton('Настройки',
                                       callback_data='settings')
#Кнопка cm_keyboard_btn_delete_post
usr_btn_mm = types.InlineKeyboardButton('Вернуться в главное меню',
                                       callback_data='main_user_menu')
#Кнопка cm_keyboard_btn_change_post


#Клавиатура cm_keyboard_main_menu
profile_menu.row(usr_btn_set,usr_btn_sub)
profile_menu.row(usr_btn_mm)