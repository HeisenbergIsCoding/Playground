import openai

openai.api_key = ""


def chat_to_bot(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion


if __name__ == '__main__':
    prompt = "老了"
    response = chat_to_bot(prompt)
    print(response.choices[0].message.content)
