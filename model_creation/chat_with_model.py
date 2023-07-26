
import openai

api_key = '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'

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



chat_with_model('how to build a house?')









# user_input = input("User: ")

# response = chat_with_model(user_input)
# print("ChatGPT: " + response)
# user_input = input("User: ")