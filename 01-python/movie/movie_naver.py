import requests
import os
import csv

def read_mv_name():
    mv_names = {}
    f = open('movie.csv', 'r', encoding='utf-8')
    rdr = csv.DictReader(f)
    for row in rdr:
        mv_names.update({row['movie_code'] : row['movie_name_ko']})
    f.close()
    return mv_names

def get_naver_movie(mv_names):
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")
    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    base_url = 'https://openapi.naver.com/v1/search/movie.json'
    mv_data = []
    
    for k, v in mv_names.items():
        url = base_url + '?query={}'.format(v)
        res = requests.get(url, headers=headers)
        data = res.json().get('items')[0]
        image = data.get('image')
        link = data.get('link')
        rating = data.get('userRating')
        mv_data.append([k, image, link, rating])
    return mv_data

def store_as_csv(mv_data, filename, fields):
    f = open(filename, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(fields)
    for row in mv_data:
        wr.writerow(row)
    f.close()

if __name__ == '__main__':
    mv_names = read_mv_name()
    mv_data = get_naver_movie(mv_names)
    fields = ['movie_code','thumb_url','link_url','user_rating']
    store_as_csv(mv_data, 'movie_naver.csv', fields)
