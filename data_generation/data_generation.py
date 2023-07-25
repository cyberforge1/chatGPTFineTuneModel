import openai
import pandas as pd
import random
import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

# Access the variables using os.getenv()
api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

# Function to generate a list of 100 unique prompts
def generate_unique_prompts():
    prompt_list = []

    # Example: Generate 100 prompts of the form "Question 1", "Question 2", ...
    for i in range(1, 101):
        prompt_list.append(f"Question {i}")

    # Shuffle the prompt list to ensure randomness
    random.shuffle(prompt_list)
    return prompt_list

# Function to interact with OpenAI API and get answers
def get_openai_responses(prompt_list):
    results = []
    for prompt in prompt_list:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use the desired GPT-3 engine
            prompt=prompt,
            max_tokens=150,  # Adjust as per your requirement
        )
        answer = response.choices[0].text.strip()
        results.append({"Prompt": prompt, "Answer": answer})
    return results

# Function to save data to an Excel file
def save_to_excel(data_list):
    df = pd.DataFrame(data_list)
    df.to_excel("output.xlsx", index=False)

if __name__ == "__main__":
    prompts = generate_unique_prompts()
    responses = get_openai_responses(prompts)
    save_to_excel(responses)