import requests
import pandas as pd
import os
from dotenv import load_dotenv
import openai

load_dotenv()

API_KEY = os.environ.get("OPENAI_KEY")
API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Function to make API requests and get completions
def get_chatGPT_completions(prompts):
    openai.api_key = API_KEY

    # Initialize a DataFrame to store prompts and completions
    df = pd.DataFrame(columns=['Prompt', 'Completion'])

    for prompt in prompts:
        response = openai.Completion.create(
            engine='text-davinci-003',  # Use the GPT-3.5 Turbo engine
            prompt=prompt,
            temperature=0.7,  # Controls the randomness of the response. Higher values make it more random.
            n=1,  # Number of responses to generate
            stop=None,  # Stop generating tokens after encountering this string
            timeout=None,  # Maximum time to wait for the API response
        )

        completion = response.choices[0].text.strip()
        print(f'Prompt: {prompt}\nCompletion: {completion}\n')

        # Append the prompt and completion to the DataFrame
        df = df._append({'Prompt': prompt, 'Completion': completion}, ignore_index=True)

    # Save the DataFrame to an Excel spreadsheet
    df.to_excel('completions.xlsx', index=False)

# Example usage with 5 prompts
get_chatGPT_completions(['Tell me a joke.', 'What is the meaning of life?', 'Explain the concept of love.', 'How does the stock market work?', 'Describe the process of photosynthesis.'])