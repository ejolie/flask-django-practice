SELECT mv_name
FROM movies
WHERE show_time >= 150;

SELECT mv_code, mv_name
FROM movies
WHERE genre = '애니메이션';

SELECT mv_name
FROM movies
WHERE country = '덴마크' AND genre = '애니메이션';

SELECT mv_name, audience
FROM movies
WHERE audience >= 1000000 AND watch_grade = '청소년관람불가';

SELECT *
FROM movies
WHERE prdt_year >= 20000101 AND prdt_year <= 20091231;

SELECT DISTINCT genre
FROM movies;