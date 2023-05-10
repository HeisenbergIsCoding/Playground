import openai
import os
import json
import configparser


def read_api_key_from_config():
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return config['API']['chatgpt_api_key']


def save_reply_content(reply_message, file_name):
    str_reply_message = json.dumps(reply_message)
    with open(file_name, 'a+', encoding="utf-8") as file:
        file.seek(0)
        if file.read(1):
            file.write("\n" + str_reply_message)
        else:
            file.write(str_reply_message)
    print("新文字已成功添加到 {} 文件。".format(file_name))


def read_contents_from_file(file_name):
    content_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file.readlines():
            load_str_to_json = json.loads(line.strip())
            content_list.append(load_str_to_json)
    return content_list


def chat_to_bot(prompt, file_name='reply.txt'):
    content_list = []

    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        content_list = read_contents_from_file(file_name)

    new_prompt = {"role": "user", "content": prompt}
    content_list.append(new_prompt)

    reply_message = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=content_list
    )
    content = reply_message.choices[0].message.content
    print(content)

    output_content = {"role": "user", "content": content}
    save_reply_content(output_content, file_name)


if __name__ == '__main__':
    openai.api_key = read_api_key_from_config()
    prompt = "你之前說的c++是怎樣的語言"
    chat_to_bot(prompt)
