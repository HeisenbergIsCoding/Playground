from pdf2docx import Converter


# 轉換pdf為docx
# 參考的文件：https://dothinking.github.io/pdf2docx/quickstart.convert.html
def convert_pdf_to_word():
    input_file_locate = 'good_game.pdf'
    output_file_locate = 'good_game.docx'
    cv = Converter(input_file_locate)
    cv.convert(docx_filename=output_file_locate)
    cv.close()


if __name__ == '__main__':
    convert_pdf_to_word()
