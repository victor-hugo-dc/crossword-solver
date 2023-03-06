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
clue = input("Which clue would you like to solve? ")
reply = chat(get_example(url)[clue])
print(reply)