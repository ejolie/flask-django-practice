# 01 Python : 영화 API를 활용한 데이터 수집

## 1. 영화진흥위원회 오픈 API

### 1) 주간/주말 박스오피스 데이터 수집

#### `movie/boxoffice.py`

최근 10주간 데이터 중 주간 박스오피스 TOP10 데이터를 수집합니다. 해당 데이터는 향후 영화평점서비스에서 기본으로 제공되는 영화 목록으로 사용될 예정입니다.

코드는 함수 단위로 구현하였으며 각 함수에 대한 설명은 다음과 같습니다.

* `get_date_range()`
  * `datetime` 모듈을 통해 기준일(2019.01.13)로부터 10주 간의 날짜를 만들어 리스트로 반환해주는 함수입니다.

* `get_boxoffice(date_range)`
  * 주간/주말 박스오피스 요청 URL에 발급받은 KOBIS API 키를 넣어줍니다. 그리고 나서 `get_date_range()` 에서 반환받은 10주 간의 날짜 데이터에 대해 for 루프를 돌면서 각 날짜를 `targetDt`에 담아 URL을 완성합니다. 
  * 이제 `requests` 모듈을 이용해 완성된 URL에 *GET* 요청을 보냅니다.
  * 결과로 받은 *response* 를 *json*으로 인코딩한 뒤 필요한 정보에 key로 접근하여 `mv_data` 에 저장합니다.
  * 이제 데이터가 담긴 `mv_data` 딕셔너리는 다음과 같이 구성됩니다.
    * Key : `영화 대표코드`
    * Value : `[영화명, 해당일 누적관객수, 해당일]` 

* `get_top_movies(my_data)`

  * 딕셔너리의 value 중 누적관객수를 기준으로 `mv_data` 를 정렬한 뒤 상위 10개(TOP10) 데이터를 반환합니다.

* `store_as_csv(mv_data, filename, fields)`

  * TOP10 데이터를 csv 파일로 저장합니다.

&nbsp;

#### `movie/boxoffice.csv`

* Fields
  * movie_code : `영화 대표코드`
  * title : `영화명`
  * audience : `해당일 누적관객수`
  * recorded_at : `해당일`



&nbsp;


### 2) 영화 상세정보 수집
#### `movie/movie.py`

* `read_mv_codes(filename)`
  * 1.1) 에서 작성한 `boxoffice.csv` 파일에서 TOP10 영화의 대표코드를 가져와 리스트로 반환합니다.

* `get_movieinfo(mv_codes)`
  * 위 함수에서 반환받은 대표코드를 하나씩 영화 상세정보 URL에 담아 요청을 보냅니다.
  * 결과로 받은 영화 상세정보를 `mv_data` 딕셔너리에 저장합니다.
    * Key : `영화 대표코드`
    * Value : [`국문 영화명`, `영문 영화명`, `원문 영화명`, `개봉연도`, `상영시간`, `장르`, `감독`, `상영등급`, `배우1`, `배우2`, `배우3`]

&nbsp;

#### `movie/movie.csv`

- Fields
  - movie_code
  - movie_name_ko
  - movie_name_en
  - movie_name_og
  - prdt_year
  - show_time
  - genres
  - directors
  - watch_grade_nm
  - actor1
  - actor2
  - actor3

&nbsp;

## 2. 네이버 영화 검색 API

### 1) 네이버 영화 데이터 수집
#### `movie/movie_naver.py`

* `read_mv_name()`
  * 1.2) 에서 작성한 `movie.csv` 파일에서 TOP10 영화의 대표코드와 국문 영화명을 가져와 `mv_names` 딕셔너리로 반환합니다
    * Key : `영화 대표코드`
    * Value : `국문 영화명`

* `get_naver_movie(my_name)`
  * 발급받은 NAVER API 키와 SECRET을 헤더에 넣어 URL을 구성합니다.
  * `read_mv_name()` 에서 반환받은 `mv_names` 딕셔너리의 Key와 Value에 대해 반복문을 돌면서 각 Value를 query에 넣어 URL에 요청을 전송합니다.
  * 결과로 받은 네이버 영화 정보를 `mv_data` 리스트에 저장합니다. 
    * `mv_data` : [ `영화 대표코드`, `썸네일 이미지 URL`, `링크 URL`, `영화 평점` ]
* `store_as_csv(mv_data, filename, fields)`
  * `mv_data` 리스트를 csv 파일로 저장합니다.

&nbsp;

#### `movie/movie_naver.csv`

* Fields
  * movie_code
  * thumb_url
  * link_url
  * user_rating

&nbsp;

### 2) 영화 포스터 이미지 저장

#### `movie/movie_poster.py`

* `get_image_link(filename)`

  * 2.2) 에서 작성한 `movie_naver.csv` 파일에서 영화 대표 코드와 링크 URL을 가져와 `links` 딕셔너리로 반환합니다.
    * Key : `영화 대표 코드`
    * Value : `링크 URL`

* `download_img(links)`

  * `links` 딕셔너리의 Key와 Value에 대해 반복문을 돌면서 영화 이미지를 저장하기 위해 각 URL에 대해 요청을 전송합니다.
  * `BeautifulSoup`를 이용해 이미지의 위치를 선택하고 요청을 전송합니다. 결과값을 `.jpg` 파일로 저장합니다.

  ```python
  with open('./images/{}.jpg'.format(code), 'wb') as f:
      f.write(img_res.content)
  ```

  

&nbsp;

#### `images/*.jpg`

`movie_poster.py` 를 통해 저장된 이미지들입니다.

&nbsp;

