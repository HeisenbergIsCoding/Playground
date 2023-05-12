import pydub
from pydub import AudioSegment


def cut_audio_length():
    # 加载音频文件
    audio = AudioSegment.from_file("test.mp3", format="mp3")

    # 要切割的时间长度（毫秒）
    duration = 30 * 1000  # 30 seconds

    # 切割音频
    chunks = [audio[i:i + duration] for i in range(0, len(audio), duration)]

    # 保存切割后的音频文件
    for i, chunk in enumerate(chunks):
        chunk.export(f"chunk{i}.mp3", format="mp3")


if __name__ == '__main__':
    cut_audio_length()
