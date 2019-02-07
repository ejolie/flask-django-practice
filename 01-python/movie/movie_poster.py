import requests
from bs4 import BeautifulSoup as bs
import os
import csv

def get_image_link(filename):
    links = {}
    f = open(filename, 'r', encoding='utf-8')
    rdr = csv.DictReader(f)
    for row in rdr:
        links.update({row['movie_code'] : row['link_url']})
    f.close()
    return links

def download_img(links):
    for code, url in links.items():
        res = requests.get(url).text
        soup = bs(res, 'html.parser')
        img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > a > img').get('src')
        img_res = requests.get(img_url)
        with open('./images/{}.jpg'.format(code), 'wb') as f:
            f.write(img_res.content)

if __name__ == '__main__':
    links = get_image_link('movie_naver.csv')
    download_img(links)