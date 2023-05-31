from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

def offers_kb(posts, n): #Передаем массив всех товаров и желаемый индекс последнего выводимого товара(по факту "строить массив" для желаемого индекса можно не в самой функции, но как по мне логически правильнее будет так)
    offers_kb = InlineKeyboardMarkup()
    if n < 0: n=0
    for i in range(n-5, len(posts)):#Так как я решил выводить только 10 позиций за раз, то от конечно индекса отнимаю 10
        if i >= n or i > len(posts):#Проверка на то когда нужно прекращать добавлять кнопки(когда индекс больше передаваемого, чтобы не выводилось больше позиций чем нужно. И проверка на то, если у последней страницы не хватает "добить" 10 позиций, оно не крашилось изза выхода за пределы массива)
            break
        else:
            cur = InlineKeyboardButton(f"{posts[i]['post_lvl_id']}) ({posts[i]['post_for']}) {posts[i]['post_name']}", callback_data="offer_id:"+str(posts[i]["post_lvl_id"])+"_"+str(posts[i]['post_for']))#Создаю кнопку в тексте которой будет отображаться количество позиции(так как до этого человек уже выбрал что именно он хочет купить), а в callback_data закидываю id продукта из бд для дальнейшего взаимодействия
            offers_kb.add(cur)#Добавляю в клавиатуру
    if n <= 5 and n >= len(posts):#Здесь идут проверки для добавления кнопок назад/вперед чтобы в конце списка не появлялась кнопка вперед
        cancel = InlineKeyboardButton("Выйти в главное меню", callback_data="main_menu")
        offers_kb.row(cancel)
    elif n == 5:
        forward = InlineKeyboardButton("Вперед", callback_data = "forward_offers" )
        cancel = InlineKeyboardButton("Выйти в главное меню", callback_data="main_menu")
        offers_kb.row(forward)
        offers_kb.row(cancel)
    elif n>=len(posts):
        back= InlineKeyboardButton("Назад", callback_data="back_offers" )
        cancel = InlineKeyboardButton("Выйти в главное меню", callback_data="main_menu")
        offers_kb.row(back)
        offers_kb.row(cancel)
    else:
        forward = InlineKeyboardButton("Вперед", callback_data = "forward_offers" )
        back= InlineKeyboardButton("Назад", callback_data="back_offers" )
        cancel = InlineKeyboardButton("Выйти в главное меню", callback_data="main_menu")
        offers_kb.row(back, forward)
        offers_kb.row(cancel)
    return offers_kb