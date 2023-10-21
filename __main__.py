# -*- coding: utf-8 -*-

from transformers import BertTokenizer
from transformers import BertForSequenceClassification
import torch
from ExcelParser import ExcelParser
from bert_classifier import BertClassifier

tokenizer_path = 'cointegrated/rubert-tiny'

model_path = 'cointegrated/rubert-tiny'

#Объект нейросети
classifier = BertClassifier(model_path, tokenizer_path)

#Считывание файлов Excel
parser = ExcelParser()
data_train = parser.Parse('DataTrain.xlsx')
data_valid = parser.Parse('DataValid.xlsx')

#Подготовка нейросети к обучению
x_train = data_train['Сообщества и подписки'].values
y_train = data_train['Шифр направления'].values
x_valid = data_valid['Сообщества и подписки'].values
y_valid = data_valid['Шифр направления'].values

classifier.preparation(x_train, y_train, x_valid, y_valid)

#Обученние
classifier.train()

#Предсказание
TesterInterests = 'Киномания Новинки кино, HD Кино - Фильмы онлайн 2023, Мемуары ценителей научных мемов, ЁП, Фильмы 2023 Новинки кино онлайн, Открытки Поздравления Пожелания С Днем Рождения, Мир Танков, Shadow Fight, Warface, Marmok, Kuplinov ► Play, Русские сериалы, фильмы, мелодрамы, Вкусные истории|Любимые Рецепты | Советы по дому, Albertina, NVIDIA, Вормикс, MSI CIS, AORUS, Телеканал 2х2, Republic of Gamers CIS, War Thunder, ZAKA-ZAKA, Д@чный советник, World of Warcraft, Steam, Epic Games, KING DM, LEGO, Батла, Xbox Россия, Манекены для рисования°|и позы, Работа в Магнитогорске, GabeStore, Сталкер / S.T.A.L.K.E.R., Кирилл Колесников, Dead by Daylight, Apex Legends, Хоккейный клуб «Металлург» Магнитогорск, Вселенная Assassins Creed, Раздачи ИГР в Epic Games Store, /folder/Games, 3d визуализация | Blog, COUGAR Russia, Наш Магнитогорск, FOXY SHOP – одежда и аксессуары, Korzov Photographer, Redragon Russia, Каргассия, Задротский Вестник, Проекты домов |Архитектура| Энергоэффективность, Притяжение, Мягкий кинотеатр г. Магнитогорск, Регион 74 | Магнитогорск, Проектирование | Обследование | Геотехника | BIM, Маркер Игрушка, Устархан Бекмурзаев, Лего Самоделки ®, Drafting Design - Дизайн Чертежи, Леруа Мерлен Магнитогорск | LEROY MERLIN, МГТУ им. Г.И. Носова, Профком студентов МГТУ им. Г. И. Носова, Союз архитекторов России, Инженерно-строительное дело. Хабаровск, Прокат Продажа Приставок Дисков Xbox PlayStation, Halo Community, ENOT – мужской шоурум, *НА ИЗГОТОВКУ* HOGIOS PROJECT, Gamer | магазин видеоигр в Магнитогорске, Russian Halo Club, Сеня Лютый, СП| MINPEN | Магнитогорск, PriRex КОФЕ и КОМИКСЫ Магнитогорск, World of Halo, Крэш битва титанов, Интернет-лицей МГТУ им. Г.И. Носова, Хало 4, ШМЯКЛЯ — Неформальный контент, Halo 5: Guardians Прохождение, Гайды, Пасхалки., Halo 3, лего хало, Крэш Бандикут, хало, [CS GO] Farm Drop Прогнозы на CS:GO, зССБ-13-01 270800.62, Пошив,ремонт одежды, PokemonRangerBoy 12, контра сити, Беловы, Бонусы от игры вормикс, Наш Магнитогорск, /folder/Games, GabeStore, Каргассия, Регион 74 | Магнитогорск, Притяжение, Мемуары ценителей научных мемов, Киномания ► Новинки кино, Задротский Вестник, HD Кино - Фильмы онлайн 2023, Телеканал 2х2, Работа в Магнитогорске, Steam, Albertina, Halo Community, Манекены для рисования°|и позы, ZAKA-ZAKA, Вселенная Assassins Creed, ЁП, ENOT – мужской шоурум' 
prediction = classifier.predict(TesterInterests)

for item in prediction:
    print(item)