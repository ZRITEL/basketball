// Баскетбол.cpp : Программа для анализа баскетбольных матчей
// kef1, kef2 вводимые коэфиценты на победы
// kef1a, kef2a выводимые значения коэфицентов в процентах
// marg выводимое значение маржи букмекера в процентах
// win1, win2 количество очных побед команд на своих площадках
// sum1, sum2 количество очных домашних матчей
// verwin1, verwin2 вероятности очной победы первой команды на своей и чужой площадке 
// sred1 средний показатель очной победы первой команды
// sum11, sum22, verwin11, verwin22, sred11 используются для перевода из double в int соответственно названиям
// ocnvst вероятность очной победы первой команды

#include "stdafx.h"
#include <iostream>

int main()
{
	double kef1, kef2;
	std::cout << std::endl; std::cout << std::endl;
	setlocale(LC_ALL, "Russian");
	std::cout << "    Вас приветствует программа для анализа баскетбольных матчей!" << std::endl;
	std::cout << std::endl;
	std::cout << "    Шаг № 1.   Введите коэфиценты для команд:" << std::endl; 
	std::cout << std::endl;
	std::cout << "    Коэфицент на победу первой команды:";
	std::cout << "    "; std::cin >> kef1;
	std::cout << "    Коэфицент на победу второй команды:";
	std::cout << "    "; std::cin >> kef2;

	int win1, win2;
	double sum1, sum2;
	std::cout << std::endl;
	std::cout << "    Шаг № 2.   Введите историю очных встречь команд:" << std::endl;
	std::cout << std::endl;
	std::cout << "    Сколько выиграла первая команда матчей на своей площадке?";
	std::cout << "    "; std::cin >> win1;
	std::cout << "    Всего было на его площадке матчей: "; std::cout << "    "; std::cin >> sum1;
	std::cout << "    Сколько выиграла вторая команда матчей на своей площадке?";
	std::cout << "    "; std::cin >> win2;
	std::cout << "    Всего было на его площадке матчей: "; std::cout << "    "; std::cin >> sum2;

	int sum11 = sum1; int sum22 = sum2;
	double verwin1 = (((win1 * 100) / sum1) + ((((win1 * 100) % sum11) / sum1) * 0.01));
	double verwin2 = 100 - ((win2 * 100) / sum2) + ((((win2 * 100) % sum22) / sum2) * 0.01);
	int verwin11 = verwin1 * 100; int verwin22 = verwin2 * 100;
	double sred1 = ((((verwin11 + verwin22) * 100) / 2) + ((((verwin11 + verwin22) % 2) / 2) * 0.01)) * 0.0001;
	int sred11 = sred1 * 100;
	double ocnvst = ((((verwin11 + sred11) * 100) / 2) + ((((verwin11 + sred11) % 2) / 2) * 0.01)) * 0.0001;

	std::cout << std::endl;
	//std::cout << "    Победа первой команды на своей площадке " << verwin1 << " %" << std::endl;
	//std::cout << "    Победа первой команды на чужой площадке " << verwin2 << " %" << std::endl;
	//std::cout << "    Средний показатель первой команды " << sred1 << " %" << std::endl;
	std::cout << "    Вероятности побед команд исходя из очных встречь:" << std::endl;
	std::cout << "    Победа первой команды: " << ocnvst << " %" << std::endl;
	std::cout << "    Победа второй команды: " << 100 - ocnvst << " %" << std::endl;
	std::cout << std::endl;

	double kef1a = 100 / kef1;
	double kef2a = 100 / kef2;
	double marg = kef1a + kef2a - 100;
	std::cout << std::endl;
	std::cout << "    Вероятности побед команд исходя из коэфицентов:" << std::endl;
	std::cout << "    Победа первой команды " << kef1a << " %" << std::endl;
	std::cout << "    Победа второй команды " << kef2a << " %" << std::endl;
	std::cout << std::endl;
	std::cout << "    Маржа букмекера равна: " << marg << " %" << std::endl;

	system("pause");
    return 0;
}

