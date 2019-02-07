# 03 DB

## 1. 테이블 구성하기

#### `01_create_table.sql`

#### 1. 해당 스키마를 가진 테이블 생성
```sql
CREATE TABLE movies (
    mv_code INTEGER PRIMARY KEY,
    mv_name TEXT,
    watch_grade TEXT,
    director TEXT,
    prdt_year INTEGER,
    audience INTEGER,
    show_time INTEGER,
    country TEXT,
    genre TEXT
);
```

#### 2. header와 mode 설정
```sql
.mode csv
.mode column
.mode tabs
.headers on
.separator ,
.import boxoffice.csv movies
```

#### 3. 전체 데이터 출력
```sql
SELECT *
FROM movies;
```





&nbsp;

## 2. 기본 CRUD 조작하기

#### `02_crud.sql`

#### 1. 영화 극한직업의 레코드를 테이블에 추가
```sql
INSERT INTO movies 
VALUES (
    20182530,
    '극한직업',
    '15세이상관람가',
    '이병헌',
    20190123,
    3138467,
    111,
    '한국',
    '코미디'
);
```

#### 2. 영화코드가 20040521인 데이터를 출력 후 해당 데이터를 삭제
```sql
SELECT * 
FROM movies
WHERE mv_code = 20040521;

DELETE FROM movies
WHERE mv_code = 20040521;
```

#### 3-1. 영화코드 20185124인 데이터를 출력
```sql
SELECT *
FROM movies
WHERE mv_code = 20185124;
```

#### 3-2. 공란으로 되어 있는 컬럼에 값을 '없음'으로 수정 후 해당 데이터의 감독이 변경되었는지 확인
```sql
UPDATE movies
SET director = '없음'
WHERE mv_code = 20185124;

SELECT director
FROM movies
WHERE mv_code = 20185124;
```





&nbsp;

## 3. 원하는 데이터 찾기

#### `03_select.sql`

#### 1. 상영시간이 150분 이상인 영화이름만 출력
```sql
SELECT mv_name
FROM movies
WHERE show_time >= 150;
```

#### 2. 장르가 애니메이션인 영화코드와 영화이름를 출력
```sql
SELECT mv_code, mv_name
FROM movies
WHERE genre = '애니메이션';
```

#### 3. 제작국가가 덴마크이고 장르가 애니메이션인 영화이름을 출력
```sql
SELECT mv_name
FROM movies
WHERE country = '덴마크' AND genre = '애니메이션';
```

#### 4. 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 영화이름과 누적관객수를 출력
```sql
SELECT mv_name, audience
FROM movies
WHERE audience >= 1000000 AND watch_grade = '청소년관람불가';
```

#### 5. 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 영화를 출력
```sql
SELECT *
FROM movies
WHERE prdt_year >= 20000101 AND prdt_year <= 20091231;
```

#### 6. 장르를 중복 없이 출력
```sql
SELECT DISTINCT genre
FROM movies;
```





&nbsp;

## 4. Expression 활용하기

#### `04_expression.sql`

#### 1. 모든 영화의 총 누적관객수 출력
```sql
SELECT audience
FROM movies;
```

#### 2. 가장 많은 누적관객수인 영화이름과 누적관객수를 출력
```sql
SELECT mv_name, MAX(audience)
FROM movies;
```

#### 3. 가장 상영시간이 짧은 영화의 장르와 상영시간을 출력
```sql
SELECT genre, MIN(show_time)
FROM movies;
```

#### 4. 제작국가가 한국인 영화의 평균 누적관객수를 출력
```sql
SELECT AVG(audience)
FROM movies
WHERE country = '한국';
```

#### 5. 관람등급이 청소년관람불가인 영화의 개수를 출력
```sql
SELECT COUNT(mv_code)
FROM movies
WHERE watch_grade = '청소년관람불가';
```

#### 6. 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력
```sql
SELECT COUNT(mv_code)
FROM movies
WHERE show_time >= 100 AND genre = '애니메이션';
```





&nbsp;

## 5. 정렬하기

#### `05_order.sql`

#### 1. 누적관객수 상위 5개 영화의 모든 데이터 출력

```sql
SELECT *
FROM movies
ORDER BY audience DESC LIMIT 5;
```



#### 2. 장르가 애니메이션인 영화를 제작국가(오름차순), 누적관객수(내림차순) 순으로 정렬하여 10개만 출력

```sql
SELECT *
FROM movies
WHERE genre = '애니메이션'
ORDER BY country ASC, audience DESC LIMIT 10;
```



#### 3. 상영시간이 긴 영화를 만든 감독의 이름을 10개만 출력

```sql
SELECT director
from movies
ORDER BY show_time DESC LIMIT 10;
```



&nbsp;