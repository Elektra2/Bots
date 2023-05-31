#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
test = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
us_test = types.InlineKeyboardButton('Начать тест🚀',
                                       callback_data='start_test')
us_skip = types.InlineKeyboardButton('Пропустить тест⏩',
                                       callback_data='skip_test')

#Клавиатура cm_keyboard_main_menu
test.row(us_test,us_skip)