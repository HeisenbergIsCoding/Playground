import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
import configparser


def read_api_key_from_config():
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return config['API']['scappingant_api_key']


def get_from_url(url):
    sa_key = read_api_key_from_config()
    sa_api = 'https://api.scrapingant.com/v2/general'
    qParams = {'url': url, 'x-api-key': sa_key}
    reqUrl = f'{sa_api}?{urllib.parse.urlencode(qParams)}'
    r = requests.get(reqUrl)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup


def download_image(url, save_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, stream=True)
    file_name = url.split('/')[-1]
    with open(os.path.join(save_path, file_name), 'wb') as handler:
        for block in response.iter_content(1024):
            if not block:
                break
            handler.write(block)
        print('圖片下載完成: ' + file_name)


def download_multiple_images(image_urls, save_path, max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_image, url, save_path) for url in image_urls]

        for future in futures:
            future.result()


def replace_download_url(original_url):
    t7_start_index = 8
    t7_end_index = 9

    t_start_index = len(original_url) - 5
    t_end_index = len(original_url) - 4

    # 使用切片和連接替換特定位置的字符串
    new_url = (
            original_url[:t7_start_index] + "i" + original_url[t7_end_index:t_start_index] + original_url[t_end_index:]
    )
    return new_url


def get_jpg_file_from_url(url, path):
    soup = get_from_url(url)
    element_id = "info"
    element = soup.find('div', id=element_id)
    find_title = element.find('h2', class_='title')
    span_elements = find_title.find_all('span')
    file_name = ''
    for span_element in span_elements:
        file_name += span_element.text.strip()
    # 建立資料夾
    if not os.path.exists(os.path.join(path, file_name)):
        os.makedirs(os.path.join(path, file_name))
        print('資料夾建立完成: ' + file_name)
    # 找需要的圖片位址
    element_id = "thumbnail-container"
    element = soup.find('div', id=element_id)
    img_elements = element.find_all('img', class_='lazyload')
    img_url_list = []
    for img_element in img_elements:
        origin_img_url = img_element['data-src']
        img_url = replace_download_url(origin_img_url)
        img_url_list.append(img_url)
    print(img_url_list)
    # 下載圖片
    download_multiple_images(img_url_list, os.path.join(path, file_name))


if __name__ == '__main__':
    # 要下載的網址
    url_list = ['']
    # 要存放的路徑
    path = ''
    for url in url_list:
        get_jpg_file_from_url(url, path)
