from openai import OpenAI
import os
import sys
import fetch_email
from dotenv import load_dotenv
load_dotenv()




def respond_to_email(mail,password):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    email = fetch_email.get_top_emails(mail,password)

    propmt = f"You are a email reponding chatbot, and I need you to respond to the following email: {email['body']}, keep in mind these special notes {notes}, the output you give should be of the folllowing form "+'{"email": a summary of the email, "response": your response to the email}'

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": propmt},
    ]
    )
    
    return completion.choices[0].message.content


if __name__ == "__main__":
    email = sys.argv[1]
    password = sys.argv[2]
    notes = sys.argv[3]
    response = respond_to_email(email, password)
    print(response)

