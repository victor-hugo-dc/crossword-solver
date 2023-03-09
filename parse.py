import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math

def scrape_page(url: str) -> BeautifulSoup:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()

    return BeautifulSoup(page, 'html.parser')

def extract_down(soup: BeautifulSoup) -> dict:
    tags = soup.findAll("td", class_="grid--cell")
    dimensions: int = int(math.sqrt(len(tags)))
    down: dict = {}

    for i in range(dimensions):
        current_down = None
        length_down = 0

        for j in range(dimensions):
            index: int = (dimensions * j) + i
            content:str = str(tags[index].contents[0])
            tag = BeautifulSoup(content, 'html.parser')
            divs = tag.find_all('div')

            if len(divs) == 2:
                down[current_down] = length_down
                current_down = None
                length_down = 0
            
            else:
                number: list = divs[2].contents
                if len(number) != 0:
                    if current_down is None:
                        current_down = number[0]
                
                length_down += 1
        
        if current_down != None:
            down[current_down] = length_down
    
    return {k: v for k, v in down.items() if k is not None}


def extract_across(soup: BeautifulSoup) -> dict:
    tags = soup.findAll("td", class_="grid--cell")
    dimensions: int = int(math.sqrt(len(tags)))
    across: dict = {}

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

    return {k: v for k, v in across.items() if k is not None} # Filter for None values

def extract_across_hints(soup: BeautifulSoup) -> dict:
    across_list = soup.findAll("div", class_="clues--list")
    across_hints = BeautifulSoup(str(across_list[0]), 'html.parser')
    clues = across_hints.findAll("div", class_="clues--list--scroll--clue")

    across_clues = {}

    for clue in clues:
        clue_ = BeautifulSoup(str(clue), 'html.parser')
        divs = clue_.find_all('div')
        number = divs[1].text
        hint = divs[2].text
        across_clues[number] = hint
    
    return across_clues

def extract_down_hints(soup: BeautifulSoup) -> dict:
    down_list = soup.findAll("div", class_="clues--list")
    down_hints = BeautifulSoup(str(down_list[1]), 'html.parser')
    clues = down_hints.findAll("div", class_="clues--list--scroll--clue")

    down_clues = {}

    for clue in clues:
        clue_ = BeautifulSoup(str(clue), 'html.parser')
        divs = clue_.find_all('div')
        number = divs[1].text
        hint = divs[2].text
        down_clues[number] = hint
    
    return down_clues


soup = scrape_page("https://www.downforacross.com/beta/game/2978701-dimp")
down = extract_down(soup)
down_hints = extract_down_hints(soup)

for k, v in down.items():
    print(f"{k}: {v}")
    print(f"What is a {v}-letter word for the clue: {down_hints[k]}")