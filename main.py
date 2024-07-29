import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv('SECRET_API_KEY')

messages = [
    {"role": "system", "content": "You are a human real estate agent sending emails to clients based on given parameters."},
]
length = input("Length of email: ")
message = input("What do you want the email to say: ")
tone = input("Tone: ")
response = input("Email to respond to: ")
     
while True:
    
    if(response == "None"):
        response = None
    content = "Please create an email in about " + length + ". With a " + tone + " about " + message + " to respond to " + response + "with no subject line"
    if message:
        messages.append(
            {"role": "user", "content": content, "temperature": 0.3},
        )
        chat = openai.chat.completions.create(
            model="gpt-3.5-turbo-16k", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    content = input("Tweaks: ")
    if (content == "none") | (content == "None"):
        break
