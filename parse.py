import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math

ACROSS = 0
DOWN = 1

def scrape_page(url: str) -> BeautifulSoup:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()

    return BeautifulSoup(page, 'html.parser')

def extract(soup: BeautifulSoup, index_fn) -> dict:
    td_tags: BeautifulSoup.ResultSet = soup.findAll("td", class_="grid--cell")
    dimensions: int = int(math.sqrt(len(td_tags)))
    lengths: dict = {}

    for i in range(dimensions):

        current = None
        length: int = 0

        for j in range(dimensions):
            index: int = index_fn(i, j, dimensions)

            tag_content = td_tags[index].contents[0]
            tag: BeautifulSoup = BeautifulSoup(str(tag_content), 'html.parser')
            divs = tag.find_all('div')

            if len(divs) == 2:
                lengths[current] = length
                current = None
                length = 0

            else:
                number: list = divs[2].contents
                if len(number) != 0:
                    if current is None:
                        current = number[0]
                
                length += 1
        
        if current != None:
            lengths[current] = length
    
    return {k: v for k, v in lengths.items() if k is not None}


def extract_clues(soup: BeautifulSoup, direction: int) -> dict:
    clues_list: BeautifulSoup.ResultSet = soup.findAll("div", class_="clues--list")
    clues_soup: BeautifulSoup = BeautifulSoup(str(clues_list[direction]), 'html.parser')
    clues_text = clues_soup.findAll("div", class_="clues--list--scroll--clue")

    clues: dict = {}

    for clue in clues_text:
        clue = BeautifulSoup(str(clue), 'html.parser')
        info = clue.find_all('div')
        clues[info[1].text] = info[2].text
    
    return clues