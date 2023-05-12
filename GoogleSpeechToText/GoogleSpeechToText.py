from google.cloud import speech
from google.oauth2 import service_account

client_file = 'key.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)


# 參考了這個影片https://www.youtube.com/watch?v=izdDHVLc_Z0
# 如果語音檔長度超過1分鐘，會出現錯誤https://stackoverflow.com/questions/44835522/why-does-my-python-script-not-recognize-speech-from-audio-file
def transcribe_file(speech_file):
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        enable_automatic_punctuation=True,
        sample_rate_hertz=16000,
        language_code="en-US"
    )
    response = client.recognize(config=config, audio=audio)
    print(response)


if __name__ == '__main__':
    transcribe_file('test1.mp3')
