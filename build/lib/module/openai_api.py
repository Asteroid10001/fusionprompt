from openai import OpenAI
import os

def prompt4o(content :str,apikey:str):
    os.environ["OPENAI_API_KEY"] = apikey
    client = OpenAI()

    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": "Say this is a test",
        }],
        model="gpt-4o",
    )

    print(response.choices[0].message.content)