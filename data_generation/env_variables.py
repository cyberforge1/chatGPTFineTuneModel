import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

# Access the variables using os.getenv()
api_key = os.getenv("OPENAI_KEY")

print("API Key:", api_key)