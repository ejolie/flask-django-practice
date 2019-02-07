import requests
import os
import datetime
import csv

def get_date_range():
    last_date = datetime.date(2019, 1, 13) 
    date_list = sorted([last_date - datetime.timedelta(weeks=x) for x in range(0, 9)])
    date_string = [x.strftime('%Y%m%d') for x in date_list]
    return date_string

def get_boxoffice(date_range):
    api_key = os.getenv('KOBIS_ID')
    weekly_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}'.format(api_key)
    mv_data = {}
    for x in date_range:
        url = weekly_url + '&targetDt={}&weekGb=0'.format(x)
        res = requests.get(url)
        boxoffice_result = res.json().get('boxOfficeResult')
        weekly_list = boxoffice_result.get('weeklyBoxOfficeList')
        for mv in weekly_list:
            mv_data.update({mv['movieCd'] : [mv['movieNm'], int(mv['audiAcc']), x]})
    return mv_data

def get_top_movies(mv_data):
    return dict(sorted(mv_data.items(), key=lambda k: k[1][1], reverse=True)[0:10])

def store_as_csv(mv_data, filename, fields):
    f = open(filename, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(fields)
    for k, v in mv_data.items():
        wr.writerow([k] + v)
    f.close()

if __name__ == '__main__':
    data_range = get_date_range()
    mv_data = get_boxoffice(data_range)
    top_movies = get_top_movies(mv_data)
    fields = ['movie_code','title','audience','recorded_at']
    store_as_csv(top_movies, 'boxoffice.csv', fields)