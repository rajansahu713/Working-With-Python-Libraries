import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']


def resolved_query(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
    )
    return response.choices[0].message['content']

print(resolved_query("Hi I am Rajan"))


## Output
"""
Hello Rajan! How can I assist you today?
"""