import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
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
    os.system("cls")

    return BeautifulSoup(page, 'html.parser')

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

# Driver code
def get_example(url):
    result = {}
    soup = scrape_page(url)
    across = extract_across(soup)
    across_hints = extract_across_hints(soup)

    for k, v in across.items():
        if k in across_hints:
            # print(f"{k}: {v}-letter word for the clue: {across_hints[k]}")
            result[k] = f"What is a {v}-letter word for the clue: {across_hints[k]}"
    return result

# get_example()