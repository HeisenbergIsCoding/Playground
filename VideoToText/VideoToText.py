from pytube import YouTube
import Config as MyConfig
import openai


# 先把影片下載成mp3
def get_video_to_mp3(url):
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    print("downloading...")
    yt.streams.filter().get_audio_only().download(filename='test.mp3')
    print("下載完成")


# 把mp3轉成文字
def get_video_txt():
    audio_file = open("test.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    text = transcript['text']
    print(text)
    en_to_cn(text)


# 把英文轉成繁體中文
def en_to_cn(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "翻譯為繁體中文" + text}
        ]
    )
    translate_content = completion.choices[0].message.content

    print(translate_content)


if __name__ == '__main__':
    openai.api_key = MyConfig.read_api_key_from_config()
    get_video_txt()
