import requests
import os
import csv
import datetime

class Movie:
    def __init__(self, mv_code, mv_name_ko, mv_name_en, mv_name_og, 
        prdt_year, show_time, genre, director, watch_grad, actors):
        self.mv_code = mv_code
        self.mv_name_ko = mv_name_ko
        self.mv_name_en = mv_name_en
        self.mv_name_og = mv_name_og
        self.prdt_year = prdt_year
        self.show_time = show_time
        self.genre = genre
        self.director = director
        self.watch_grad = watch_grad
        self.actors = actors

class MovieDB: 
    def __init__(self, last_date):
        self.last_date = last_date # datetime.date(2019, 1, 13) 
        self.date_range = []
        self.keys = {}
        self.boxoffice = {}
        self.top_movies = {}

    def set_API_keys(self):
        self.keys.update({'KOBIS_ID' : os.getenv('KOBIS_ID')})
        self.keys.update({'NAVER_CLIENT_ID' : os.getenv('NAVER_CLIENT_ID')})
        self.keys.update({'NAVER_CLIENT_SECRET' : os.getenv('NAVER_CLIENT_SECRET')})

    def get_API_keys(self, key):
        return self.keys.get(key)

    def set_date_range(self):
        date_list = sorted([self.last_date - datetime.timedelta(weeks=x) for x in range(0, 9)])
        self.date_range = [x.strftime('%Y%m%d') for x in date_list]

    def get_date_range(self):
        return self.date_range

    def set_boxoffice(self):
        weekly_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}'.format(self.get_API_keys['KOBIS_API'])
        for date in self.get_date_range():
            url = weekly_url + '&targetDt={}&weekGb=0'.format(date)
            res = requests.get(url)
            boxoffice_result = res.json().get('boxOfficeResult')
            weekly_list = boxoffice_result.get('weeklyBoxOfficeList')
            for mv in weekly_list:
                self.boxoffice.update({mv['movieCd'] : [mv['movieNm'], int(mv['audiAcc']), date]})

    def get_boxoffice(self):
        return self.boxoffice

    def set_top_movies(self, num):
         self.top_movies = dict(sorted(self.movies.items(), key=lambda k: k[1][1], reverse=True)[0:num])

    def get_top_movies(self):
        return self.top_movies

    def get_mv_codes(self):
        return list(self.top_movies.keys())

    def set_movieinfo(self):
        info_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}'.format(self.get_API_keys['KOBIS_API'])
        for mv_code in self.get_mv_codes():
            url = info_url + '&movidCd={}'.format(mv_code)
            res = requests.get(url)
            mv_info = res.json().get('movieInfoResult').get('movieInfo')
            mv_name_ko = mv_info.get('movieNm')       # 영화명 -국문
            mv_name_en = mv_info.get('movieNmEn')     # -영문
            mv_name_og = mv_info.get('movieNmOg')     # -원문
            prdt_year = mv_info.get('prdtYear')       # 제작연도
            show_time = mv_info.get('showTm')         # 상영시간
            genres = '/'.join([g['genreNm'] for g in mv_info.get('genres')])
            watchgrad = mv_info.get('audits')[0].get('watchGradeNm')
            directors = '/'.join([d['peopleNm'] for d in mv_info.get('directors')])   # 감독명
            act1, act2, act3 = [p.get('peopleNm') for p in mv_info.get('actors')[:3]] # 배우
            movie = new Movie(mv_code, mv_name_ko, mv_name_en, mv_name_og, 
        prdt_year, show_time, genre, director, watch_grad, actors)
            self.

    def store_as_csv(self, filename, fields):
        f = open(filename, 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow(fields)
        for k, v in self.top_movies.items():
            wr.writerow([k] + v)
        f.close()

#         self.last_date = datetime.date(2019, 1, 13) 