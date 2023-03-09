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

url = input("Please paste the URL of the crossword: ")
try:
    soup = scrape_page(url)
    across = extract_across(soup)
    across_hints = extract_across_hints(soup)

    for k, v in across.items():
        reply = chat(f"What is a {v}-letter word for the clue: {across_hints[k]}")
        print(f"{k}a: {reply}")

except:
    print("Please provide a valid downforacross url.")