#Импорты
from aiogram import types


#Клавиатура "Админ Панель главное меню"
admin_panel_keyboard_main_menu = types.InlineKeyboardMarkup()
#Кнопка admin_panel_btn_create_post
ap_btn_cp = types.InlineKeyboardButton('Создать пост',
                                       callback_data='create_post')
ap_btn_ct = types.InlineKeyboardButton('Создать тест',
                                       callback_data='create_test')
#Кнопка admin_panel_btn_delete_post

#Кнопка admin_panel_btn_change_post
ap_btn_chp = types.InlineKeyboardButton('Изменить пост',
                                       callback_data='change_post')
#Кнопка admin_panel_btn_make_user_role
ap_btn_mur = types.InlineKeyboardButton('Назначить роль пользователю',
                                       callback_data='make_user_role')
ap_btn_drfu = types.InlineKeyboardButton('Удалить роль у пользователя',
                                       callback_data='delete_role_from_user')
#Добавляем кнопки в клавиатуру
admin_panel_keyboard_main_menu.row(ap_btn_mur)
admin_panel_keyboard_main_menu.row(ap_btn_drfu)
admin_panel_keyboard_main_menu.row(ap_btn_cp, ap_btn_chp)
admin_panel_keyboard_main_menu.row(ap_btn_ct)
