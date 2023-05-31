#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
writing_menu = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
us_materials = types.InlineKeyboardButton('Написать эссе',
                                       callback_data='writing_essay')
#Кнопка cm_keyboard_btn_change_post
us_profile = types.InlineKeyboardButton('Посмотреть написанные эссе',
                                       callback_data='show_essay')

usr_btn_mm = types.InlineKeyboardButton('Вернуться в главное меню',
                                       callback_data='main_user_menu')


#Клавиатура cm_keyboard_main_menu
writing_menu.row(us_materials, us_profile)
writing_menu.row(usr_btn_mm)