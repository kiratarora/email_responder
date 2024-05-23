from openai import OpenAI
import os
import fetch_email
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

email = fetch_email.get_top_emails(1)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"You are a email reponding chatbot, and I need you to respond to the following email: {email['body']}"},
  ]
)

print(completion.choices[0].message)

