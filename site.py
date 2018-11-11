import requests

#Блок загрузки страницы по ссылке пользователя
site = str(input("Введите ссылку на матч с сайта www.myscore.ru :\n"))  # Получаем ссылку на сайт от пользователя
url = requests.get(site)   #  Загружаем интернет страницу по ссылке пользователя
html = url.text        #  Переводим страницу в текст (в строку)

#Блок загрузки страницы с таблицей
posit = site.find("match-summary")
site = site[0:posit]
site_tabl = site + "standings;table;overall"
url = requests.get(site_tabl)
html_tabl = url.text

# Блок вывода загаловка страницы
start = html.find("<title>") + 7   # Определяем позицию первого символа загаловка
finish = html.find("</title>")     # Определяем позицию последнего символа заголовка
title = html[start:finish]            # Запоминаем в строку заголовок
print("Вы выбрали матч ", title)                              # Выводим заголовок

#Блок вывода домашней команды
home = html.find("<div class=\"team-text tname-home\">")
start = html.find("return false;\">", home) + 15
finish = html.find("</a>", start)
team_1 = html[start:finish]
print("Команда 1: ", team_1)

#Блок вывода гостевой команды
home = html.find("<div class=\"team-text tname-away\">")
start = html.find("return false;\">", home) + 15
finish = html.find("</a>", start)
team_2 = html[start:finish]
print("Команда 2: ", team_2)

