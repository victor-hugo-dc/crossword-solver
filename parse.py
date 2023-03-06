# from bs4 import BeautifulSoup
# import urllib.request
# from selenium import webdriver

# url = "https://www.downforacross.com/beta/game/2965282-thrun"
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, features="html.parser")
# print(soup)
# tags = soup.findAll("td", class_="grid--cell")
# print(tags)

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

url = "https://www.downforacross.com/beta/game/2965282-thrun"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
os.system("cls")

soup = BeautifulSoup(page, 'html.parser')
tags = soup.findAll("td", class_="grid--cell")    

clues = soup.findAll("div", class_="clues--list--scroll--clue")
print(tags[0])
print(type(tags[0]))
print(clues[0])