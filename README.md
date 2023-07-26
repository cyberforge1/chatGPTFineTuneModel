# Python Project: Custom Data Generation and Fine-tuned ChatGPT Model

This Python project aims to generate custom data by calling the OpenAI GPT-3 API and then use this data to create a chatbot using a finely-tuned GPT-3 model.

*** The instructions in this guide are closely based on OPENAI's Resources available at the following link: https://platform.openai.com/docs/guides/fine-tuning ***

## Prerequisites

Before running the project, make sure you have the following:

1. An OpenAI GPT-3 API key: You can sign up for the OpenAI API and get your key.
2. Python and required libraries: Ensure you have Python installed along with the `openai`, `openpyxl`, and `dotenv` libraries. Install them using the following command:

```bash
pip install openai openpyxl python-dotenv
```

## Setup

1. Clone the repository or create a new Python file to implement the project.
2. Create a `.env` file in the project directory and set your OpenAI API key as follows:

```plaintext
OPENAI_KEY=your_openai_api_key_here
```

## Project Overview

The project consists of two main parts:

1. Generating Custom Data: The `chat_with_gpt3` function is used to generate custom data by calling the OpenAI GPT-3 API with a given prompt and receiving a poetic-style response.
2. Creating a Fine-tuned ChatGPT Model: The `chat_with_model` function utilizes the finely-tuned GPT-3 model to respond to user queries.

## Usage

### 1. Generating Custom Data

The function `process_excel_file` reads data from an Excel file containing prompts and appends the responses generated using the `chat_with_gpt3` function. The data is then saved back to the same Excel file.

To use this function, follow these steps:

1. Prepare an Excel file with prompts in column A (starting from the second row).
2. Run the `process_excel_file` function by providing the filename as an argument.

```python
file_name = 'prompt_data.xlsx'
process_excel_file(file_name)
```

### 2. Using the Fine-tuned Model

The `chat_with_model` function uses the fine-tuned GPT-3 model to respond to user queries. Simply call this function with a user message as the input.

```python
response = chat_with_model('how to build a house?')
print("ChatGPT: " + response)
```

### Additional Bash Commands

The following are some useful commands for fine-tuning models and interacting with the OpenAI API:

```bash
# Installing openai library and setting up the API key
pip install --upgrade openai
export OPENAI_API_KEY="your_openai_api_key_here"

# Preparing data for fine-tuning
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>

# Creating a fine-tuned model
openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>

# Resuming model event stream continuation
openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>

# Associated commands for fine-tuning models
openai api fine_tunes.list
openai api fine_tunes.get -i <YOUR_FINE_TUNE_JOB_ID>
openai api fine_tunes.cancel -i <YOUR_FINE_TUNE_JOB_ID>

# Using the fine-tuned model with bash
openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
```

Note: Replace placeholders such as `<OPENAI_API_KEY>`, `<LOCAL_FILE>`, `<TRAIN_FILE_ID_OR_PATH>`, `<BASE_MODEL>`, `<YOUR_FINE_TUNE_JOB_ID>`, `<FINE_TUNED_MODEL>`, and `<YOUR_PROMPT>` with appropriate values as per your use case.

Remember to consult the official OpenAI API documentation for detailed information on using their services and APIs.

