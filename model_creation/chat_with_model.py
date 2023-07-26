
import openai
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key



def chat_with_model(message):
    response = openai.Completion.create(
        prompt=message,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        model="davinci:ft-personal-2023-07-26-01-45-21"  # The fine-tuned model ID
    )
    print(response.choices[0].text.strip())
    return response.choices[0].text.strip()



chat_with_model('tell me about the cosmos?')


