import requests
import time

#Блок загрузки страницы по ссылке пользователя
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
site = str(input("Введите ссылку на матч с сайта www.myscore.ru :\n"))  # Получаем ссылку на сайт от пользователя
url = requests.get(site, headers=headers, timeout=10)   #  Загружаем интернет страницу по ссылке пользователя
html = url.text        #  Переводим страницу в текст (в строку)

#Блок загрузки страницы с таблицей
posit = site.find("match-summary")
site = site[0:posit]
site_tabl = site + "standings;table;overall"
url = requests.get(site_tabl, headers=headers, timeout=10)
html_tabl = url.text

#Блок загрузки страницы с коэфицентами
site_kx = site + "odds-comparison;home-away;ft-including-ot"
url = requests.get(site_kx, headers=headers, timeout=10)
html_kx = url.text

#Блок с поиском коэфицентов
start = html.find("<td class=\"kx o_1\">")
print(start)
finish = html.find("class=\"odds-wrap\"", start) + 28
print(finish)
kx_1 = html[finish:finish + 4]
start = html.find("<td class=\"kx o_2\">")
print(start)
finish = html.find("class=\"odds-wrap\"", start) + 28
print(finish)
kx_2 = html[finish:finish + 4]

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
print("Коэфицент на П1: ", kx_1)

#Блок вывода гостевой команды
home = html.find("<div class=\"team-text tname-away\">")
start = html.find("return false;\">", home) + 15
finish = html.find("</a>", start)
team_2 = html[start:finish]
print("Команда 2: ", team_2)
print("Коэфицент на П2: ", kx_2)

#Тест с выводом страницы в документ
file = open("test.txt", "w")
file.write(html_kx)
file.close()
