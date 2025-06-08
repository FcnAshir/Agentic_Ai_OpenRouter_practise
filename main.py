import os
from openai import OpenAI
from dotenv import load_dotenv

# API Key Load Karna
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Client Banayein
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

while True:
    # User se Input Le
    user_input = input("Aapka Sawal: ")
    # Request bhejna
    response = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct",  # yeh free model hai
    messages=[
        {"role": "user", "content": f"Ashir sir mujhe yeh batayein: {user_input}"}
    ],
  
)


# Output print karna
    print(response.choices[0].message.content)
    if user_input.lower() == "exit":
        print("Program band ho gaya.")
        break

