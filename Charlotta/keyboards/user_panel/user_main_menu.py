#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
user_main_menu = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
us_materials = types.InlineKeyboardButton('EduCourse📒',
                                       callback_data='show_material')
#Кнопка cm_keyboard_btn_change_post
us_profile = types.InlineKeyboardButton('Your profile🪪',
                                       callback_data='show_profile')
wr = types.InlineKeyboardButton('Essays📝',
                                callback_data='writing')


#Клавиатура cm_keyboard_main_menu
user_main_menu.row(us_profile)
user_main_menu.row(us_materials, wr)