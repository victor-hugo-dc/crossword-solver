import openai
import re
from config import key

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


length = input("How many letters? ")
message = input("Clue: ")
message = f"{length}-letter word for the crossword clue: {message}"

reply = chat(message)
print(reply)

try:
    word = re.findall(r'"([^"]*)"', reply)[0]
    # here get rid of all the periods and spaces
    print(word)
except:
    print(" ")