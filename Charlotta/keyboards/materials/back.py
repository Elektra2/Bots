#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
back_to_list = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
ar_btn_yes = types.InlineKeyboardButton('Back',
                                       callback_data='materials')

#Клавиатура cm_keyboard_main_menu
back_to_list.row(ar_btn_yes)
