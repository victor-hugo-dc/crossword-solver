import openai
from config import key
from parse import *

openai.api_key = key

messages = [{
        "role": "system",
        "content": "You solve crossword clues."
    }]

def chat(message: str) -> str:
    global messages
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

if __name__ == '__main__':
    url = input("Please paste the URL of the crossword: ")
    try:
        soup = scrape_page(url)

        down = lambda i, j, dimensions: (dimensions * j) + i
        across = lambda i, j, dimensions: (dimensions * i) + j

        dlengths = extract(soup, down)
        alengths = extract(soup, across)

        dclues = extract_clues(soup, DOWN)
        aclues = extract_clues(soup, ACROSS)

        for k, v in dlengths.items():
            reply = chat(f"What is a {v}-letter word for the clue: {dclues[k]}")
            print(f"{k} DOWN: {reply}")
        
        for k, v in alengths.items():
            reply = chat(f"What is a {v}-letter word for the clue: {aclues[k]}")
            print(f"{k} ACROSS: {reply}")

    except:
        print("Please provide a valid downforacross url.")