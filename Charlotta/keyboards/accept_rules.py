#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
accept_rules_menu = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
ar_btn_yes = types.InlineKeyboardButton('Принять',
                                       callback_data='accept')
#Кнопка cm_keyboard_btn_delete_post
ar_btn_no = types.InlineKeyboardButton('Отклонить',
                                       callback_data='not_accpet')

#Клавиатура cm_keyboard_main_menu
accept_rules_menu.row(ar_btn_yes, ar_btn_no)
