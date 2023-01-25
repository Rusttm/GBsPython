"""
программа имеет GUI интерфейс для внесения и просмотра записей в базу сотрудников
при этом запись и чтение осуществляются в модуле MysqlconnectionModule.py
база данных развернута на Docker образе и начально заполняется с помощью файлов
MysqlinitModule - инициализация
MysqlfillModule - заполнение
"""

import MysqlconnectionModule as sqlconnector
import tkinter as tk

