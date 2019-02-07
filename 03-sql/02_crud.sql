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

SELECT * 
FROM movies
WHERE mv_code = 20040521;

DELETE FROM movies
WHERE mv_code = 20040521;

SELECT *
FROM movies
WHERE mv_code = 20185124;

UPDATE movies
SET director = '없음'
WHERE mv_code = 20185124;

SELECT director
FROM movies
WHERE mv_code = 20185124;