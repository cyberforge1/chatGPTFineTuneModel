
import openai

api_key = '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'

openai.api_key = api_key



def chat_with_model(message):
    response = openai.Completion.create(
        engine='ada:ft-personal-2023-07-20-13-30-18',  # Specify the engine to use (e.g., text-davinci-003)
        prompt=message,
        #max_tokens=200,  # Adjust the number of tokens in the response as needed
        temperature=0.7,  # Controls the randomness of the response. Higher values make it more random.
        n=1,  # Number of responses to generate
        stop=None,  # Stop generating tokens after encountering this string
        timeout=None,  # Maximum time to wait for the API response
    )
    print(response)
    return response.choices[0].text.strip()





chat_with_model('is this working?')









# user_input = input("User: ")

# response = chat_with_model(user_input)
# print("ChatGPT: " + response)
# user_input = input("User: ")