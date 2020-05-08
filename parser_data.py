import requests
from bs4 import BeautifulSoup
import re
import urllib
import os

#Сегодня мы будем писать парсер любого сайта https://www.combook.ru/

path_now = os.getcwd() #получаем текущую директорию
URL = input("Введите страницу, которую вы хотите спарсить: \n")
URL = URL.strip()
name_folder = input("Введите название папки, в которую вы хотите все складывать: \n")
os.mkdir(name_folder)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
