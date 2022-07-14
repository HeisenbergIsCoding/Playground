from wordcloud import WordCloud


# 建一個文字雲來玩玩
# api reference:https://amueller.github.io/word_cloud/references.html
def create_wordcloud():
    with open('words.txt') as f:
        text = f.read()

    wd = WordCloud().generate(text=text)
    image_cloud = wd.to_image()
    image_cloud.show()


if __name__ == '__main__':
    create_wordcloud()
