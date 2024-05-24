from openai import OpenAI
import os
import sys
from dotenv import load_dotenv
load_dotenv()




def get_recipe():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    propmt = f"You are a smart chef, and I want you to suggest a recepie for a dish with the following ingredients: {ingredients}, and keep in mind the following dietary restrictions {restrictions}."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": propmt},
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


if __name__ == "__main__":
    ingredients = sys.argv[1]
    restrictions = sys.argv[2]
    response = get_recipe()

