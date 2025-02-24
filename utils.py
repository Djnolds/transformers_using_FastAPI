from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
    )

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    response = client.chat.completions.create(
            messages=messages,
            model="gpt-4o-mini",
    )

    reply = response.choices[0].message.content
    return reply