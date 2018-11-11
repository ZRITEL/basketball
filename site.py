import requests

site = str(input("Введите ссылку на матч с сайта www.myscore.ru :\n"))
url = requests.get(site)
htmltext = url.text
start = htmltext.find("<title>") + 7
finish = htmltext.find("</title>")
S1 = htmltext[start:finish]
print(S1)
