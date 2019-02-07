import requests
import os
import csv
from boxoffice import store_as_csv

def read_mv_codes(filename):
    mv_codes = []
    f = open(filename, 'r', encoding='utf-8')
    rdr = csv.DictReader(f)
    for row in rdr:
        mv_codes.append(row['movie_code'])
    f.close()
    return mv_codes

def get_movieinfo(mv_codes):
    api_key = os.getenv('KOBIS_ID')
    info_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}'.format(api_key)
    mv_data = {}
    for cd in mv_codes:
        url = info_url + '&movieCd={}'.format(cd)
        res = requests.get(url)
        mv_info = res.json().get('movieInfoResult').get('movieInfo')
        
        mv_name_ko = mv_info.get('movieNm')       # 영화명 -국문
        mv_name_en = mv_info.get('movieNmEn')     # -영문
        mv_name_og = mv_info.get('movieNmOg')     # -원문
        # open_year = mv_info.get('openDt')[:4]   # 개봉연도
        prdt_year = mv_info.get('prdtYear')       # 제작연도
        show_time = mv_info.get('showTm')         # 상영시간
        genres = '/'.join([g['genreNm'] for g in mv_info.get('genres')])
        watchgrad = mv_info.get('audits')[0].get('watchGradeNm')
        directors = '/'.join([d['peopleNm'] for d in mv_info.get('directors')])   # 감독명
        act1, act2, act3 = [p.get('peopleNm') for p in mv_info.get('actors')[:3]] # 배우
        mv_data.update({cd : [mv_name_ko, mv_name_en, mv_name_og, prdt_year, show_time, genres, directors, watchgrad, act1, act2, act3]})
    return mv_data

if __name__ == '__main__':
    mv_codes = read_mv_codes('boxoffice.csv')
    mv_data = get_movieinfo(mv_codes)
    fields = ['movie_code','movie_name_ko','movie_name_en','movie_name_og','prdt_year','show_time','genres','directors','watch_grade_nm','actor1','actor2','actor3'
    ]
    store_as_csv(mv_data, 'movie.csv', fields)