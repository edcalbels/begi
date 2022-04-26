# # pattern - правила(архитектура,пародигмы)
# # паттерны нужны для того чтобы валидировать


# # валидность - правильность


# import re

# # re - regular Expression - регулярные выражения которые предоставляют шаблон
# # у регулярныхх выражений есть свой алфавит символов который нужен для чего-то

# # """title@gmal.com"""


# # """

# # (com|ru)
# # """


# # email = input('Email ')


# # is_valid = re.search(r"[a-zA-Z0-9]+@(gmail|mail|yandex)\.(com|ru)",email)
# # print(is_valid)





# # (gmail|mail|yandex) gruppirovka.

# # *Что сделал:
# # Дз 6
# # *Проблемы:
# # были с лямбдами
# # Помог ментор
# # *Что буду делать :
# # Смотреть видео 
# # *Исполнитель:
# # Салиев Дастан

# phone = input('phone number')

# is_valid = re.search(r"\+996-([0-9]{3})-",phone)
# print(is_valid)


