import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import math

url = "https://www.downforacross.com/beta/game/2965282-thrun" # beta url for testing
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

dimensions: int = int(math.sqrt(len(tags)))
across: dict = {
    # index of clue : length of solution
}
down: dict = {
    # index of clue : length of solution
}


for k in range(dimensions):
    current_across = None
    length_across = 0

    for i in range(dimensions):
        index: int = (dimensions * k) + i
        content: str = str(tags[index].contents[0])
        tag = BeautifulSoup(content, 'html.parser')
        divs = tag.find_all('div')

        # Reset when we encounter a black square
        if len(divs) == 2:
            across[current_across] = length_across

            current_across = None
            length_across = 0
        
        else:
            number: list = divs[2].contents
            if len(number) != 0:
                if current_across is None:
                    current_across = number[0]
            
            length_across += 1

    if current_across != None:
        across[current_across] = length_across

print(across)